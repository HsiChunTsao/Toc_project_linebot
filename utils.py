import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(userID, text):
    line_bot_api = LineBotApi('wOqAo4vLG22WznL32Drzi/KWNskOwRWP+H/kcPgyM7dymPwBqKAb+U9rL3I38L30rWM1tbafSt/oK54o+pFs8pVP52kdvALZB68E8ezrVF4gWXDHFAEZmLnjt0ejphDZVjB908obbu5Y/R4XWbeKQwdB04t89/1O/w1cDnyilFU=')
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    line_bot_api.push_message(userID, TextSendMessage(text=text))
    return "OK"

def send_image_message(userID, original_content_url, preview_image_url):
    line_bot_api = LineBotApi('wOqAo4vLG22WznL32Drzi/KWNskOwRWP+H/kcPgyM7dymPwBqKAb+U9rL3I38L30rWM1tbafSt/oK54o+pFs8pVP52kdvALZB68E8ezrVF4gWXDHFAEZmLnjt0ejphDZVjB908obbu5Y/R4XWbeKQwdB04t89/1O/w1cDnyilFU=')
    line_bot_api.push_message(userID, ImageSendMessage(original_content_url=original_content_url , preview_image_url=preview_image_url))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
