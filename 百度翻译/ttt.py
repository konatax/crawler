import requests
#这个包不用逆向
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",

}
data = {
    "kw": "dog"
}
resp = requests.post(url, headers=headers, data=data)
print(resp.text)