import requests

# 圖片檔案的路徑
image_path = '/workspaces/cycu_ai2024/map.png'

# LINE Notify API 的 URL
url = "https://notify-api.line.me/api/notify"

# 您的 LINE Notify 令牌
token = 'zsssHlD4rr3b00v04ylY1kADXX8aiD18LdpeGQBwrBt'

# 設定請求頭，包含您的 LINE Notify 令牌
headers = {
        "Authorization": "Bearer " + token
}

# 設定要發送的訊息和圖片檔案
data = {
        'message': "吳奕辰"
}
files = {
        'imageFile': open(image_path, 'rb')
}

# 發送 POST 請求
response = requests.post(url, headers=headers, data=data, files=files)

# 關閉檔案
files['imageFile'].close()

# 檢查回應
print(response.status_code)
print(response.text)