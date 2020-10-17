from pyquery import PyQuery as pq
#PyQueryクラスをpqという名前でインポート
d = pq(filename = 'index.html',encoding='utf-8')#パースとはプログラムのソースコードやXML文書など、一定の文法に従って記述された複雑な構造の
#テキスト文書を解析し、プログラムで扱えるようなデータ構造の集合体に変換することである。
#print(d)
d = pq(url='http://example.com/',encoding='utf-8')
#print(d)
#文字列を指定してパースすることも可能
d = pq("""
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
    </html>""")
#sprint(d)