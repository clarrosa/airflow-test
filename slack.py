import os
from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

client = WebClient(token=SLACK_BOT_TOKEN)
channel_id = CHANNEL_ID

result = client.chat_postMessage(
channel=channel_id, 
text='@canal La cosa está corriendo bien con el pod')
