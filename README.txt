[[[TwitchGodotVenv]]]

This repository contains a Python virtual environment configured for a Twitch-to-Godot Bot project using Twitchio, Asyncio, and WebSockets. Below are the details of the virtual environment and its configuration:

[Python Version]

•	Python 3.12.3

[Packages]

The following packages are installed in this virtual environment:

•	aiohttp 3.9.5
•	aiosignal 1.3.1
•	asyncio 3.4.3
•	attrs 23.2.0
•	frozenlist 1.4.1
•	idna 3.7
•	iso8601 2.1.0
•	multidict 6.0.5
•	pip 24.0
•	twitchio 2.9.1
•	typing_extensions 4.11.0
•	websockets 12.0
•	yarl 1.9.4

[Setup Instructions]

1. Activate the Virtual Environment:
	source TwitchGodotVenv/bin/activate

2. Verify the Python Version:
	python --version

3. Check Installed Packages:
	pip list

[Environment Variables]

To securely manage your Twitch Bot’s Access Token, set the Environment Variable as follows:

1. Open your shell configuration file:
	nano ~/.zshrc   # For Zsh

2. Add the following line:
	export TWITCH_ACCESS_TOKEN="YOUR_NEW_ACCESS_TOKEN"

3. Apply the changes:
	source ~/.zshrc

In your script, retrieve the Access Token from the Environment Variable:

import os
import twitchio

access_token = os.getenv("TWITCH_ACCESS_TOKEN")
channel = "#TWITCH_CHANNEL"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=access_token, prefix='!', initial_channels=[channel])

if __name__ == "__main__":
    bot = Bot()
    bot.run()

[Obtaining a Twitch Access Token]

Follow these steps to obtain a proper Access Token via curl commands in the Terminal, using your Registered Twitch Application’s Client ID and Client Secret:

1. Generate Authorization URL:
Open the following URL in your browser, replacing YOUR_CLIENT_ID with your actual Client ID:

https://id.twitch.tv/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost&response_type=code&scope=chat:read%20chat:edit

2. Authorize the Application:
Log in to Twitch and Authorize the Application. After authorization, you will be redirected to your Redirect URI (e.g., http://localhost) with an authorization code in the URL. Copy the code parameter from the URL.

3. Exchange Authorization Code for Access Token:
Run the following command in your Terminal, replacing YOUR_CLIENT_ID, YOUR_NEW_CLIENT_SECRET, AUTHORIZATION_CODE, and REDIRECT_URI with your actual values:

curl -X POST 'https://id.twitch.tv/oauth2/token' \
-d 'client_id=YOUR_CLIENT_ID' \
-d 'client_secret=YOUR_NEW_CLIENT_SECRET' \
-d 'code=AUTHORIZATION_CODE' \
-d 'grant_type=authorization_code' \
-d 'redirect_uri=http://localhost'

4. Validate the New Access Token:
Run the following command in your Terminal, replacing YOUR_NEW_ACCESS_TOKEN with the actual Access Token you received:

curl -H "Authorization: Bearer YOUR_NEW_ACCESS_TOKEN" \
"https://id.twitch.tv/oauth2/validate"

These steps will allow you to securely generate and validate a new Access Token for your Twitch-to-Godot Bot.