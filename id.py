import os
from slackclient import SlackClient

BOT_NAME='server-status'

sc = SlackClient(os.environ.get('SBT'))

if __name__ == "__main__":
    api_call= sc.api_call("users.list")
    if api_call.get("ok"):
        users = api_call.get("members")
        for u in users:
            if 'name' in u and u.get('name') == BOT_NAME:
                print("Bot ID for '" + u['name'] + "' is " + u.get('id'))
    else:
        print("Unable to find a bot with the name " + BOT_NAME) 
