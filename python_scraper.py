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
    books = sctape(html,url)
    save('books.csv', books)

def fetch(url: str) -> str:
    r = requests.get(url)
    return r.text #HTTPヘッダーから取得したエンコーディングででコードした文字列を返す。
    print(r)

def scrape(html: str, base_url: str) ->list[dict]
    