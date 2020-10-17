import sys
import requests

url = sys.argv[1]#コマンドラインから得る
r = requests.get(url)
print(f'encoding: {r.encoding}', file=sys.stderr)
print(r.text)