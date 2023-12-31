import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create a client instance
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

# The ID of the user you want to send to
user_id = "U06BTMG78J2"

# The path to the file you want to upload
file_path = "./worryuguu.png"

try:
    # Call the files.upload method using the WebClient
    # The file will be uploaded and sent to the user_id
    result = client.files_upload(channels=user_id, file=file_path)
    assert result["file"]["id"]
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
