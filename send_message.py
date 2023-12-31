import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create a client instance
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

# The name of the channel you want to send to
# channel_id = "python"
channel_id = user_id = "U06BTMG78J2"

try:
    # Call the chat.postMessage method using the WebClient
    # The text will be posted to the channel_id
    result = client.chat_postMessage(channel=channel_id, text="Hello world!")
    assert result["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
