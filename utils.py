import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(userID, text):
    line_bot_api = LineBotApi('I8+o9kNpFclYwrfQz/xtJ0Ot/lKf2awbgwWLR2wH6BiZY5aUWCAzTbcF1rj5q56268Gsp7mEiYZNmdmjaKHTDQgbCJ8KbpiQ8fOG/zBcT3h1rFOnJn90WPc0zP6SRuHsmJxcveVGcOj3rt01yhAIGAdB04t89/1O/w1cDnyilFU=')
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    line_bot_api.push_message(userID, TextSendMessage(text=text))
    return "OK"

def send_image_message(userID, original_content_url, preview_image_url):
    line_bot_api = LineBotApi('I8+o9kNpFclYwrfQz/xtJ0Ot/lKf2awbgwWLR2wH6BiZY5aUWCAzTbcF1rj5q56268Gsp7mEiYZNmdmjaKHTDQgbCJ8KbpiQ8fOG/zBcT3h1rFOnJn90WPc0zP6SRuHsmJxcveVGcOj3rt01yhAIGAdB04t89/1O/w1cDnyilFU=')
    line_bot_api.push_message(userID, ImageSendMessage(original_content_url=original_content_url , preview_image_url=preview_image_url))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
