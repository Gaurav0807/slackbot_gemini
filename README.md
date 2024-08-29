
# Integrating Slack Bot with an LLM-based Chatbot using Gemini Model and ngrok
  This project demonstrates how to integrate a Slack bot with a Large Language Model (LLM)-based chatbot using Google's Gemini model. The integration allows for intelligent and context-aware communication directly within Slack.

![Alt text](<Slack Chatbot Arch.jpeg>)
# Project Overview
The Slack bot is built using Python and Flask and is integrated with an LLM-powered chatbot utilizing the Gemini model. This setup enables the bot to process user inputs in Slack channels and respond 
intelligently based on the latest data engineering information.

# Key Components
# 1. Slack Bot Setup
   Libraries Used: slack_sdk, slack_bolt
   Functionality: The bot listens for app_mention events triggered when someone mentions the bot in a Slack channel.
   Configuration: Tokens and secrets are securely loaded from a .env file using environment variables

# 2. Flask Integration
     Flask App: The Flask app handles incoming HTTP requests from Slack.
     Event Processing: Slack events are processed through Flask using SlackRequestHandler from the slack_bolt.adapter.flask module.

# 3. Gemini Model Integration
     Gemini Model: The Gemini model, provided by Google's Generative AI platform, processes and responds to queries.
     Python Package: The google.generativeai package is used to interact with the Gemini model, allowing for prompt-based queries.
     Configuration: Tokens are securely loaded from a .env file using environment variables for geminiai api.

# 4. ngrok Setup
   ngrok Usage: ngrok provides a public URL that forwards requests to the local Flask application, enabling Slack to communicate with the bot.
   Setup Command: ngrok http 6060 is used to expose the Flask app to the internet.

# Result
The integration results in a Slack bot capable of performing advanced data analysis and responding intelligently to user queries within Slack.
