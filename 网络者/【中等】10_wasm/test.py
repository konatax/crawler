import pywasm
import requests
import time

# wasm_url = 'http://spider.wangluozhe.com/static/wasm/main10.wasm'
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#         'cookie': 'session=85fa876c-984a-4e55-8426-d32588907af4.uY_ISWk0OFIYlPQBuplTQv2lyNY'
#     }
# content = requests.get(wasm_url, headers=headers).content
#
# with open('./main10.wasm', 'wb') as f:
#     f.write(content)
# # timestamp = int(time.time()*1000)
vm = pywasm.load('main10.wasm')
print('ok')
# # result = vm.exec('resume', [timestamp,])
# # print(result)
