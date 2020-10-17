import json

cities = [
    ['1', '上海', '24150000'],
    ['2', 'カラチ', '23500000'],
    ['3', '北京', '21516000'],
    ['4', '天津', '14722100'],
    ['5', 'イスタンブル', '14160467'],
]

print(json.dumps(cities))
print(json.dumps(cities, ensure_ascii=False, indent=2))

with open('top_cities.json','w') as f:
    json.dump(cities, f)