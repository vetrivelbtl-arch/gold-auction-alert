import os
import requests

BOT_TOKEN = os.getenv("ARCH")
CHAT_ID = os.getenv("GOLDAUCTION_DGL_BOT")

message = """🏦 Gold Auction Bot

Bot is running successfully.

Next step:
Add bank auction websites and send notifications automatically.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
