import lxml.html
tree = lxml.html.parse('dp.html')
tree = lxml.html.parse(open('dp.html',encoding="utf-8"))#windows環境ではデフォルトの標準出力はCP932への変換が行われる
print(type(tree))
html = tree.getroot()
print(type(html))

html = lxml.html.fromstring("""
    <html>
    <head><title>八百屋オンライン</title></head>)
    <body>
    <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
    <ul>
        <li>りんご</li>
        <li class="featured">みかん</li>
        <li>ぶどう</li>
    </ul>
    </body>
    </html>""")#fromstringで文字列をパースできる。プログラムで扱えるようなデータ構造に変換すること

print(type(html))
print(html.xpath('//li'))
print(html.cssselect('li'))
print(html.cssselect('li.featured'))

h1 = html.cssselect('h1')[0]
print(h1.tag)#タグの名前を取得できる
print(h1.get('id'))
print(h1.attrib)
print(h1.getparent())
strong = h1.cssselect('strong')[0]
print(strong.text)
print(strong.tail)
print(h1.text)
print(h1.tail)
print(h1.text_content())#要素内の全てのテキストを結合した文字列が得られる