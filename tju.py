import time
import requests
# import BeautifulSoup
from bs4 import BeautifulSoup

def kill_captcha(data):
    with open('captcha.png', 'wb') as fp:
        fp.write(data)
    return raw_input('please enter the captcha(in captcha.png): ')

def login(username, password, oncaptcha):
    session = requests.session()

    captcha_content = session.get('http://e.tju.edu.cn/Kaptcha.jpg').content

    data = {
        'uid': username,
        'password': password,
        'captchas': oncaptcha(captcha_content)
    }

    resp = session.post('http://e.tju.edu.cn/Main/logon.do', data).content
    return session

if __name__ == '__main__':
    user = raw_input("user: ")
    password = raw_input("password: ")
    session = login(user, password, kill_captcha)
    print BeautifulSoup(session.get("http://e.tju.edu.cn").content).prettify()
