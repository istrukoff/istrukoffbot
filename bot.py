import requests
from time import sleep

API_KEY = "545651028:AAGEFgdAOtXWaz7ADRjdN4YIjcWnJqYC1TY"

url = str.format("https://api.telegram.org/bot{key}/", key = API_KEY)


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(str.format('{url}sendMessage', url = url), data = params)
    return response


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_message(get_chat_id(last_update(get_updates_json(url))), 'Hello, my friend!')
           update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()
