import re
from html import unescape
from urllib.parse import urljoin
#ダウンロードしたファイルを開き、中身を変数htmlに格納する
with open('dp.html','r',encoding="utf-8") as f:#withを使うと自動でファイルを閉じる
    html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = urljoin('https://gihyo.jp/', url)#相対urlを絶対urlに変える

    #書籍のタイトルは、itemprop="name"という属性を持つp要素から取得する。

    title = re.search(r'<p itemprop="name".*?</p>',partial_html).group(0)
    title = title.replace('<br/>',' ')#brタグをスペースに置き換える
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title) # 文字参照が含まれている場合は元に戻す

    print(url, title)