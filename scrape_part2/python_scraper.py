import csv
from typing import List #型ヒントのためにインポート

import requests
import lxml.html

def main():
    """
    メインの処理。fetch(),scrape,save()の３つの関数を呼び出す
    """

    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html,url)
    save('books.csv', books)

def fetch(url: str) -> str:
    r = requests.get(url)
    return r.text #HTTPヘッダーから取得したエンコーディングででコードした文字列を返す。

def scrape(html: str, base_url: str) ->List[dict]:
    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content() #wbr要素などが含まれる

        books.append({'url': url, 'title': title})

    return books

def save(file_path: str, books: List[dict]):
    """
    引数booksで与えられた書籍のリストをCSV形式のファイルに保存する。
    ファイルのパスは引数file_pathで与えられる。
    戻り値:なし
    """

    with open(file_path, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, ['url', 'title'])
        writer.writeheader() #1行目のヘッダーを出力する
        # writerows()で複数の行を一度に出力する。引数は辞書のリスト。
        writer.writerows(books)

# pythonコマンドで実行された場合にmain()関数を呼び出す。これはモジュールとして他のファイルから
# インポートされたときに、main()関数が実行されないようにするための、Pythonにおける一般的なイディオム。
if __name__ == '__main__':
    main()