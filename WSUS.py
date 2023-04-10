import requests
import warnings
import subprocess


def Web():
    urls = {"WSUS": "http://192.168.1.249:8530"
            }
    for name, url in urls.items():
        # 以下兩行關閉告警，需載入warnings，預防中間人攻擊
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                response = requests.get(url, verify=False)
                response.raise_for_status()
                print(name, "連線成功", url)
            except requests.exceptions.RequestException as e:
                print(name, "連線失敗", url, ":", e)
                subprocess.run(['shutdown', '/r', '/t', '0'])
                print('WSUS 主機正在重新啟動…')
