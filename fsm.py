from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_message

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
        return text.lower() != "index"

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
        url = 'https://www.dcard.tw/f/'+a[0]
        if(int(a[1]) > 30):
            reply_token = event.reply_token
            send_text_message(reply_token, "抓太多囉")
            self.go_back()
        else:
            reg_imgur_file  = re.compile('http[s]://imgur.dcard.tw/\w+\.(?:jpg|png|gif)')
            res = requests.get(url)
            soup = BeautifulSoup(res.text,'html.parser')
            articles = soup.select('div.NormalPostLayout__TitleWrapper-sc-1kpmwi8-4.eSrfAB h3')
            articles2 =  soup.select('div.PostList_entry_1rq5Lf a')
            x = 0
            for art in articles[:int(a[1])]:
                art2 = articles2[x]
                reply_token = event.reply_token
                send_text_message(reply_token, art.text + "\n" +'https://www.dcard.tw'+art2['href'])
                print(art.text)
                print('https://www.dcard.tw'+art2['href'])
                res = requests.get('https://www.dcard.tw'+art2['href'])
                images = reg_imgur_file.findall(res.text)
                print(images)
                for image in set(images):
                        ID = re.search('http[s]://imgur.dcard.tw/(\w+\.(?:jpg|png|gif))',image).group(1)
                        print(ID)
                        send_image_message(reply_token, image)
                x = x+1
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
        send_image_message(reply_token, "https://imgur.dcard.tw/QcbRYCc.jpg")
        self.go_back()

    def on_exit_index(self):
        print("Leaving index")
