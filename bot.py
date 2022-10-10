# Libraries
import os
import re

from requests import ReadTimeout, get
from telegram_bot.TelegramBot import TelegramBot
from dotenv import load_dotenv


def replace_string(row_dict: dict, string: str) -> str:
    """Remove excess format strings with no keys"""
    to_be_replaced = re.findall(r"\{(.*?)\}", string)
    for format_string in to_be_replaced:
        if format_string not in row_dict.keys():
            continue
        string = string.replace(
            f"{{{format_string}}}", row_dict[format_string])
    return string


def post_to_telegram(token: str, group_id: str, message: str, image: str = None, **kwargs) -> None:
    """Post to Telegram"""
    bot = TelegramBot(token)
    if image is None:
        return bot.send_message(message, group_id)
    return bot.send_image(message, group_id, image)


def get_status(url, timeout=1):
    """Get status of the website"""
    try:
        response = get(url, timeout=timeout)
        return response.status_code, response.json()
    except ReadTimeout:
        return 408, "Website timed out"


if __name__ == '__main__':
    load_dotenv()
    TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
    GROUP_ID = os.getenv("GROUP_ID")
    URL = os.getenv("URL")
    print("Starting...")

    # Get the latest data from the API
    print("Visiting Frontend")
    fe_status, fe_data = get_status(URL)
    print("Received Frontend Response")
    print("Visiting Backend")
    be_status, be_data = get_status(URL + "/admin")
    print("Received BackEnd Response")

    response = post_to_telegram(TELEGRAM_API_TOKEN, GROUP_ID, f"""
Frontend Status:
Status Code: {fe_status}
Server is {'up' if fe_status == 200 else f'down {fe_status}: {fe_data}'}

Backend Status:
Status Code: {be_status}
Server is {'up' if be_status == 200 else f'down {be_status}: {be_data}'}""")
