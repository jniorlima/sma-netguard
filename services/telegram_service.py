import requests

import config


def send(message):

    if config.TELEGRAM_TOKEN == "":
        return

    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"

    requests.post(

        url,

        data={

            "chat_id": config.CHAT_ID,

            "text": message

        }

    )