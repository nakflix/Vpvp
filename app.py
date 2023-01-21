import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://nakflix: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@github.com/nakflix/File-sharing-Bot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
