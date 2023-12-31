import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create a client instance
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

try:
    # Call the users.list method using the WebClient
    # This will return a list of all users in the workspace
    result = client.users_list()

    # Loop through the users and print their ID and name
    for member in result["members"]:
        print(f'ID: {member["id"]}, Name: {member["name"]}')

except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
