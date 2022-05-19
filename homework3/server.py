# save this as app.py
import time
import requests
import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'Вставить текст',
        'flag': 0
    })

def bot(helper):
    response = {'name': 'Подручный', 'text': None, 'time': time.time(), 'flag': 2}
    if helper == '/list':
        response['text'] = 'Список команд:\n' \
                           '/help - подсказывает, как выйти из программы\n' \
                           '/anon - анонимный режим'
    elif helper == '/help':
        response['text'] = 'Чтобы выйти из программы, нажмите alt + f4'

    if response['text']:
        db.append(response)


@app.route("/")
def hello():
    return "Добро пожаловать на мой сервер!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db
    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']
    flag = data['flag']
    message = {
        'text': text,
        'name': name,
        'time': time.time(),
        'flag': flag
    }
    db.append(message)
    if flag != 2:
        bot(text)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    users = set()
    msg_cnt = 0
    for m in db:
        msg_cnt += 1
        if m['flag'] != 2:
            users.add('<li>' + m['name'] + '</li>')

    return "<center><h1>Все работает:</h1>" \
           "<p><big>Список пользователей: {users}</big></p>" \
           "<p><big>Количество пользователей: {user_cnt}</big></p>" \
           '<img src="https://cdn0.iconfinder.com/data/icons/tiny-icons-1/100/tiny-06-512.png" </center>' \
           "<p><mark>Количество сообщений: {msg_cnt}</mark></p>".format(
            user_cnt = len(users),
            users = ''.join(users),
            msg_cnt = msg_cnt
    )

app.run()
