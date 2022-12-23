import telegram.ext
import requests
import json

TOKEN = '5812881560:AAFqejbg8UBE15hW1CkyK7Ne61zglQlEzNQ'



def start(update, context):
    update.message.reply_text('''Hello Welcome, Find the nearest airport by inputting the longitude and latitude ''')
    text = update.message.text
    link = "https://api.checkwx.com/station/lat/" + text + "/lon/-73.99"
    hdr = {"X-API-Key": "95e4e3daef1e40a9b3c6194f1d"}
    req = requests.get(link, headers=hdr)
def content(update, context):
    update.message.reply_text('leave')

def handle_message(update, context):
    update.message.reply_text('мы не смогли найти ваш запрос')
    try:
        req.raise_for_status()
        resp = json.loads(req.text)
        update.message.reply_text(json.dumps(resp, indent=1))
    except requests.exceptions.HTTPError as e:
        print(e)
    start()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('content', content))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

#text = input()
#link = "https://api.checkwx.com/station/lat/" + text + "/lon/-73.99"

hdr = {"X-API-Key": "95e4e3daef1e40a9b3c6194f1d"}
#req = requests.get(link, headers=hdr)

print("Response from CheckWX.... \n")

#try:
    #req.raise_for_status()
   # resp = json.loads(req.text)
   # print(json.dumps(resp, indent=1))

#except requests.exceptions.HTTPError as e:
    #print(e)


updater.start_polling()
updater.idle()
