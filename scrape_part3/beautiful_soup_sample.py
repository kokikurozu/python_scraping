from bs4 import BeautifulSoup
with open('dp.html', encoding="utf-8") as f:
    soup = BeautifulSoup(f, 'html.parser')
#BeautifulSoup()にはファイル名やurlを指定できない。第2引数にパーサー名を指定する。
soup = BeautifulSoup("""
<html>
<head><title>八百屋オンライン</title></head>
<body>
<h1 id ="main"><strong>おいしい</strong>今日のくだもの</h1>
<ul>
    <li>りんご</li>
    <li class = "featured">みかん</li>
    <li>ぶどう</li>
</ul>
</body>
</html>""", 'html.parser')
print(soup.h1)