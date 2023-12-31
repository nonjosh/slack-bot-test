import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create a client instance
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

# The ID of the user you want to send to
user_id = "U06BTMG78J2"

# Define the attachment
attachment = [
    {
        "fallback": "Required plain-text summary of the attachment.",
        "color": "#36a64f",
        "pretext": "Optional text that appears above the attachment block",
        "author_name": "Bobby Tables",
        "author_link": "http://flickr.com/bobby/",
        "title": "Slack API Documentation",
        "title_link": "https://api.slack.com/",
        "text": "Optional text that appears within the attachment",
        "fields": [{"title": "Priority", "value": "High", "short": False}],
        "image_url": "http://my-website.com/path/to/image.jpg",
        "thumb_url": "http://example.com/path/to/thumb.png",
        "footer": "Slack API",
        "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
        "ts": 123456789,
    }
]

try:
    # Call the chat.postMessage method using the WebClient
    # The text will be posted to the user_id with the attachment
    result = client.chat_postMessage(
        channel=user_id, text="Hello world!", attachments=attachment
    )
    assert result["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
