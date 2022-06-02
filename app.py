#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('E3XH/yG8mOECD07YGOHUt26BpIow6fKGXNqvMj40OLkg9Kl8809YDLr7xnUZ+H313IemZLdT4ltb5YEygN4bcmZOhOxxz73rP0eMDmx7ReoBwEax3tVrRPqvzjfBnGRMiauRouWwW66sCJkVY6zIiQdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('a6cf8ccce5aa3ad4a795cf8de93800d1')

	
line_bot_api.push_message('Ue45389146f3ec58fe6cc267fb101d05d', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
 
    return 'OK'
