from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นายนัฐวุฒิ หงษ์กลาย เลขที่3 ม.4/1"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded[' originaldetectintentrequest '][' โหลด '][' ข้อมูล '][' replytoken ']
    userText = decoded[' queryresult '][' เจตนา '][' name ']
    #sendText(user,userText)
    if (userText == 'สวัสดี') :
         sendText(user,'ค่ะ')
    elif (userText == 'บาย') :
         sendText(user,'เจอกันใหม่นะ')
    else :
         sendText(user,'คืออะไรเหรอ')
    
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
