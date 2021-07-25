from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent, VideoSendMessage, ImageSendMessage

import configparser
import exp_lib
import json
import requests

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('C:/Users/SCKao/Desktop/exp/linebot/config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel-access-token'))
handler = WebhookHandler(config.get('line-bot', 'channel-secret'))


def richmenu():
    headers = {"Authorization": "Bearer " + config.get('line-bot', 'channel-access-token'),
               "Content-Type": "application/json"}
    body = json.load(open("C:/Users/SCKao/Desktop/exp/linebot/files/richmenu.json", 'r', encoding='utf-8'))
    req = requests.request('POST', "https://api.line.me/v2/bot/richmenu", headers=headers,
                           data=json.dumps(body).encode('utf-8'))
    a = req.text[15:56]
    with open("C:/Users/SCKao/Desktop/exp/linebot/files/rich_menu.png", 'rb') as f:
        line_bot_api.set_rich_menu_image(a, "image/jpeg", f)
    req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/' + a, headers=headers)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global message_count
    message_count += 1
    text = event.message.text

    if text == '使用者心情':
        response = exp_lib.find_exp(event.message.text, event.source.user_id)
    elif text == '推薦音樂':
        response = exp_lib.recommond_music(event.message.text, event.source.user_id)
    elif text == '梗圖':
        response = exp_lib.recommond_meme(event.message.text, event.source.user_id)
    else:
        response = '格式錯誤！'
    print(event.source.user_id + ': ' + event.message.text)
    # 回覆文字訊息
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=response + '\n Message num ' + str(message_count)))
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Message num ' + str(message_count)))


@handler.add(PostbackEvent)
def handle_postback(event):
    global message_count
    message_count += 1
    data = event.postback.data
    userid = event.source.user_id

    if data == "video":  # 影片推薦
        response = exp_lib.recommond_music('推薦音樂', event.source.user_id)
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=response + '\n Message num ' + str(message_count)))

    elif data == "emotion":  # 心情
        response = exp_lib.find_exp("使用者心情", event.source.user_id)
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=response + '\n Message num ' + str(message_count)))

    elif data == "meme":  # 梗圖
        response = exp_lib.recommond_meme('梗圖', event.source.user_id)
        image_message = ImageSendMessage(
            original_content_url=response,
            preview_image_url=response
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    else:
        response = '格式錯誤！'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=response + '\n Message num ' + str(message_count)))

    print(userid + ': ' + "使用者心情")


if __name__ == "__main__":
    richmenu()
    message_count = 0
    app.run(debug=True)
