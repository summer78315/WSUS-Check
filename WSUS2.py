import requests
import warnings
import subprocess

# 設定 Line Notify 的權杖
# PIXIS 耀億 六人群裡
token = 'vNV3UPGuglClosci3x8zXztYXkveRMimu3KFIVWstsV'
# 設定 Line Notify 的權杖
# token = "GuyqYAYiI9WJhm5e0RNNJZXA3GgiJ4h2rErS5yN4MSK"


def Web():
    urls = {"WSUS": "http://192.168.1.249:8530"}

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
                # 發送 Line Notify 訊息
                message = f"{name} 連線失敗，錯誤訊息：{e}，60s後將重新啟動服務"
                headers = {"Authorization": f"Bearer {token}"}
                payload = {"message": message}
                requests.post("https://notify-api.line.me/api/notify",
                              headers=headers, data=payload)
                # 延遲 1 分鐘後重新啟動主機
                subprocess.run(['shutdown', '/r', '/t', '60'])
                print('WSUS 主機正在重新啟動…')
