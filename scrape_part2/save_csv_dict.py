import csv

#ファイルを書き込み用に開く。newline=''として改行コードの自動変換を抑制する。
with open('top_cities5.csv','w',newline='',encoding="utf-8") as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population']) # csv.writerはファイルオブジェクトを引数に指定する。
    writer.writeheader()
    #writerows()で複数の行を一度に出力する。引数はリストのリストへ
    writer.writerows([
        {'rank':'1','city': '上海', 'population':'24150000'},
        {'rank':'2','city': 'カラチ','population': '23500000'},
        {'rank':'3','city': '北京', 'population': '21516000'},
        {'rank':'4','city': '天津', 'population':'14722100'},
        {'rank':'5','city': 'イスタンブル', 'population':'14160467'},
    ])#辞書のkeyは保存されない