import os
import time
import subprocess
import re
from slackclient import SlackClient

Id = os.environ.get('BID')

at = "<@"+ Id + ">"
slack_client = SlackClient(os.environ.get('SBT'))

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
            else:
                print("Connection failed. Check your Slack token, bot ID, and internet link.")

def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API is an events firehose.
    this parsing function returns None unless a message is
    directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return None, None

def handle_command(command, channel):
    if command.startswith("status"):
        cmd = re.sub("", '', command).trim()
        slack_client.api_call("chat.postMesasge", channel=channel, text=response, as_user=True)
