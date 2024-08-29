import os
import logging
from flask import Flask, request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import load_dotenv
load_dotenv()
from analyzer.prompt_analyzer import gemini_model_call


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Slack Bot Integartion with LLM based Chatbot")

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]

app = App(token=SLACK_BOT_TOKEN)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

def get_bot_user_id():
    try:
        # Initialize the Slack client with your bot token
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")


def my_function(text):
    response = text.upper()
    return response

@app.event("app_mention")
def handle_mentions(body,say):

    text = body["event"]["text"]
    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()
    say("Sure, I'll get right on that!")

    response = gemini_model_call(text)

    say(response)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    logger.info("Incoming HTTP Request *******************************************************")
    return handler.handle(request)



if __name__=="__main__":
    flask_app.run(debug=True)
