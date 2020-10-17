from urllib.parse import urljoin
from bs4 import BeautifulSoup

#HTMLファイルを読み込んでBeautifulSoup
with open('dp.html', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

#select()メソッドで、セレクターに該当するa要素のリストを取得して、個々のa要素に対して処理を行う。

for a in soup.select('#listBook > li > a[itemprop="url"]'):
    url = urljoin('https://gihyo.jp/dp', a.get('href'))
#書籍の退路つは itemprop="name"という属性のp要素を取得する。

    p = a.select('p[itemprop="name"]')[0]
    title = p.text # wbr要素などが含まれるので、stringではなくtextを使う。

    # 書籍のURLとタイトルを出力する。
    print(url, title)
