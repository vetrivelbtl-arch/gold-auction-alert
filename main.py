importimport os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.getenv("ARCH")
CHAT_ID = os.getenv("GOLDAUCTION_DGL_BOT")

DISTRICTS = [
    "Dindigul",
    "Palani",
    "Madurai",
    "Theni",
    "Usilampatti"
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
