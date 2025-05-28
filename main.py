from eitaa.main import Bot
from re import match, IGNORECASE, findall,search
import requests
if requests.get("https://raw.githubusercontent.com/zbatmanz/Api/refs/heads/main/App.json").json()["result"] == True:
	pass
else:
	print("source Off")
	exit()
bot = Bot("chrome",True)



result,baner = [],""
def get_idj(baner):
    global id
    try:
        ms = bot.chats()
        print(ms)
        for mv in ms.keys():
            bot.send_message(mv,baner)
        bot.send_message(id,"به تمامی چت های مورد نظر شما ارسال شد.")
    except:pass
while True:
    try:
        bot.go_chat(id)
        msg = bot.onchatupdate()["result"]
       
        if not msg["message_id"] in result:
            result.append(msg["message_id"])
            text:str = msg["text"]
            print(msg)
            if text == "/start":
                bot.send_message(id,"hello is bot startd")
                
            elif text.startswith("بنر"):
                bot.send_message(id,"برای تنظیم بنر خود بنر را با گزاشتن + اول متن ارسال کنید.")
            elif text.startswith("+"):
                baner = text[1:]
                bot.send_message(id,"بنر تنظیم شد.\nبرای شروع دستور (شروع) یا (Start) را ارسال کنید.")
            elif match(r'^(Start|شروع)$', text, IGNORECASE):
            	bot.send_message(id,"شروع سند کردن لطفا منتظر بمانید.")
            	get_idj()
    except:pass