import time
import requests


TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)# 一時的なエラーを表すステータスコード

def main():
    """
    メインとなる処理。
    """
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error!')

def fetch(url: str) -> requests.Response:
    """
    指定したURLにリクエストを送り、Responseオブジェクトを返す。
    一時的なエラーが起きた場合は、最大3回リトライする。
    3回リトライしても成功しなかった場合は、例外Exceptionを発生させる。
    """
    max_retries = 3 #最大で3かいリトライする。
    retries = 0 #現在のリトライ回数を示す変数。
    while True:
        try:
            print(f'Retrieving{url}...')
            response =requests.get(url)
            print(f'Status: {response.status_code}')
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response #一時的なエラーでなければresponseを返して終了。

        except requests.exceptions.RequestException as ex:
            # ネットワークレベルのエラーの場合はログを出力してリトライする。
            print(f'Network-level exception occured: {ex}')
        #リトライ処理
        retries += 1
        if retries >= max_retries:
            raise Exception('Too many retries.') #リトライ回数の上限を越えた場合は例外処理を発生させる。

        wait = 2**(retries - 1)#指数関数的なリトライを行う方が、サーバに負荷をかけない

        print(f'Waiting{wait}seconds...')
        time.sleep(wait) #time.sleepは引数秒分動作を待つ

if __name__ ==  '__main__':
    main()