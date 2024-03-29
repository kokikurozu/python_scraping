import csv

#ファイルを書き込み用に開く。newline=''として改行コードの自動変換を抑制する。
with open('top_cities2.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f) # csv.writerはファイルオブジェクトを引数に指定する。
    writer.writerow(['rank', 'city', 'population'])
    #writerows()で複数の行を一度に出力する。引数はリストのリストへ
    writer.writerows([
        ['1', '上海', '24150000'],
        ['2', 'カラチ', '23500000'],
        ['3', '北京', '21516000'],
        ['4', '天津', '14722100'],
        ['5', 'イスタンブル', '14160467'],
    ])