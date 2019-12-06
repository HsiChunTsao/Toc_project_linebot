from transitions.extensions import GraphMachine

from utils import send_text_message

import requests 
from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.request import urlretrieve

#
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
#

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_board(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_article(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
    
    def is_going_to_index(self, event):
        text = event.message.text
        return text.lower() == "index"

    def on_enter_board(self, event):
        print("I'm entering board")
        a = event.message.text.split(" ",1)
        print(a[0])
        url = 'https://www.dcard.tw/'+a[0]
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger board")
        self.go_back()

    def on_exit_board(self):
        print("Leaving board")

    def on_enter_article(self, event):
        print("I'm entering article")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger article")
        self.go_back()

    def on_exit_article(self):
        print("Leaving article")

    def on_enter_index(self, event):
        print("I'm entering index")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger index")
        self.go_back()

    def on_exit_index(self):
        print("Leaving index")
