#robot.txt、クローリングが許可されているのか教えてくれる。許可されているのならTrue、されていないならfalse

url_allow = 'https://www.amazon.co.jp/ref=nav_logo' #確認したいurlを入力

import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url(url_allow)
rp.read()
print(rp.can_fetch('mybot', 'https://www.python.org/'))

