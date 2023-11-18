import os
import re
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.chat_models import ChatOpenAI

load_dotenv()

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_mention(event, say):
    user=event["user"]
    thread_ts = event["ts"]
    mention_text = re.sub("<@.*>", "", event["text"])
    llm = ChatOpenAI(
     model_name=os.environ["OPENAI_API_MODEL"],
     temperature=os.environ["OPENAI_API_TEMPERATURE"],
     )
    response =  llm.predict(mention_text)
    response2 =  thread_ts
    say(text= f"こんにちは<@{user}>さん,{response}", thread_ts=thread_ts)
    #say(thread_ts=thread_ts,text=f"Hi there, <@{user}>!")
# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()