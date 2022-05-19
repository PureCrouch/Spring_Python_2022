import requests
import time


name = input('Введите имя: ')
print('Добро пожаловать в чат, ', name, ', Чтобы получить доступ к командам, напишите /list')
while True:
    flag = 0
    text = input('Введите сообщение: ')
    if text == '/anon':
        flag = 1
        text = input('Введите сообщение: ')
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text,
                                 'flag': flag
                             }
                            )