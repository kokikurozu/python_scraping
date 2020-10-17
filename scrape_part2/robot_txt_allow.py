#robot.txt、クローリングが許可されているのか教えてくれる。許可されているのならTrue、されていないならfalse

url_allow = 'https://baseball.yahoo.co.jp/npb/game/2020100902/stats' #確認したいurlを入力

import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url(url_allow)
rp.read()
print(rp.can_fetch('mybot', 'https://www.python.org/'))

