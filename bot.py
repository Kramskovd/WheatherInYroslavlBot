import requests


class WheatherBot:
    def __init__(self, token):
        self.token = token
        self.url = 'https://api.telegram.org/bot{}/'.format(self.token)

    def get_updates(self, offset=None, timeout=30):
        parameters = {'timeout': timeout, 'offset': offset}
        res = requests.get(self.url + 'getUpdates', parameters)
        return res.json()['result']

    def get_last_update(self):
        res = self.get_updates()

        if len(res) > 0:
            return res[-1]
        if len(res) == 0:
            return False

        return res[len(res)]

    def send_message(self, chat_id, message):
        parameters = {'chat_id': chat_id, 'text': message}
        response = requests.post(self.url + 'sendMessage', data=parameters)
        return response