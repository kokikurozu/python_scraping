import sys
import requests
import re

url = sys.argv[1]
r = requests.get(url)
scanned_text = r.content[:1024].decode('ascii',errors='replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)