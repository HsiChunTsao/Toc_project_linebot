import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


from fsm import TocMachine
from utils import send_text_message



load_dotenv()


machine = TocMachine(
    states=["user", "board", "index"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "board",
            "conditions": "is_going_to_board",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "index",
            "conditions": "is_going_to_index",
        },
        {
            "trigger": "go_back",
            "source": ["board", "index"],
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
#channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
#if channel_secret is None:
#    print("Specify LINE_CHANNEL_SECRET as environment variable.")
#    sys.exit(1)
#if channel_access_token is None:
#    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
#    sys.exit(1)

line_bot_api = LineBotApi('pFaw0u18MzAna8ZIF6Eby7Hm6mEHkLpamUocVb/+iiqv7UYRN/GDcW8Z5s2SllDlPXxMFMNjetkk1glMdW+qoVIItHrvB9926qSGWoM514NXPMoultRhfrYctZ9x7TW5hjKD76EUJ4NgenCj68liYQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('966d7c10f2d5761649ad7a93cecaf2ae')


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="123" + event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請輸入要抓取的看板代碼：\n並輸入要抓取前幾篇熱門文章的圖片(至多30篇)\nEx:抓取攝影版前兩篇文章圖片則輸入：\nphotography 2\n可輸入index查詢看板代碼")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
