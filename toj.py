'''
querying all accepted submissions of some user on toj
and save in "id.csv" sorted in submitted time order
'''

import time
import urllib
import re
from bs4 import BeautifulSoup

user = raw_input('Enter user id: ')
# url = 'http://acm.tju.edu.cn/toj/status.php?user=' + user
url = 'http://acm.tju.edu.cn/toj/status.php?accept=1&user=' + user

probid = []

while True:
    print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    probs = soup.find_all("tr", align="center", height="30")
    for prob in probs:
        probid.append(prob.find("a", href=re.compile("showp.*html")).get_text())

    nextPage = soup.find("a", text=re.compile(".*Next Page.*"))
    suffix = nextPage.get('href')
    url = 'http://acm.tju.edu.cn/toj/' + suffix
    if url.endswith('start=-1'):
        break
    #don't give too much pressure to the server =.=
    time.sleep(0.8)

f = open(user + ".csv", "w+")
for i in reversed(probid):
    f.write(i + "\n")
f.close()
