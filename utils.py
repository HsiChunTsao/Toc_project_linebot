import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi('pFaw0u18MzAna8ZIF6Eby7Hm6mEHkLpamUocVb/+iiqv7UYRN/GDcW8Z5s2SllDlPXxMFMNjetkk1glMdW+qoVIItHrvB9926qSGWoM514NXPMoultRhfrYctZ9x7TW5hjKD76EUJ4NgenCj68liYQdB04t89/1O/w1cDnyilFU=')
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    line_bot_api.push_message("U4d2e2a8faa714e3829623eb823b3e2ec", TextSendMessage(text=text))
    return "OK"

def send_image_message(reply_token, original_content_url, preview_image_url):
    line_bot_api = LineBotApi('pFaw0u18MzAna8ZIF6Eby7Hm6mEHkLpamUocVb/+iiqv7UYRN/GDcW8Z5s2SllDlPXxMFMNjetkk1glMdW+qoVIItHrvB9926qSGWoM514NXPMoultRhfrYctZ9x7TW5hjKD76EUJ4NgenCj68liYQdB04t89/1O/w1cDnyilFU=')
    line_bot_api.push_message("U4d2e2a8faa714e3829623eb823b3e2ec", ImageSendMessage(original_content_url=original_content_url , preview_image_url=preview_image_url))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
