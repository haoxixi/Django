
import json,time
import requests

# url = "https://oapi.dingtalk.com/robot/send?access_token=5c198e400fe6217744436b9c040b3ddbea271c6195dd5c2b45fb86e5b4ae6f8f"
# url = "https://oapi.dingtalk.com/robot/send?access_token=739cdc134a4021dfe673a5ba5b73e772af3da26d94c246a93d9d16fdf7f8658e"
url = "https://oapi.dingtalk.com/robot/send?access_token=a075f0ba6d45bee2e45076ed0a7df19b22d6072f451f6e0aa2a4158ac8ce3f9e"
headers = {
    "Content-Type": "application/json",
    "Charset": "utf-8"
}

requests_data = {
    "msgtype": "text",
    "text": {
        "content": "靓仔，借个火"
    },
    "at": {
        "atMobiles": [
        ],
        "isAtAll": True
    }
}
while True:
    sendData = json.dumps(requests_data)

    response = requests.post(url = url,headers = headers, data = sendData)

    content = response.json()

    print(content)
    time.sleep(2)


