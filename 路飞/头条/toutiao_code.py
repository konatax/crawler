import time
import execjs
import requests

node = execjs.get()
with open('sdk2.js','r',encoding='utf-8') as f:
    code = f.read()
cxt = node.compile(code)

current_time = int(time.time())
# print(current_time)

for i in range(5):
    targetUrl = f'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398972&max_behot_time={current_time}&refresh_count=2&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web'
    current_time -= 25
    print('=====================================================')
    # print(targetUrl)
    funcName = 'getSignature("{0}")'.format(targetUrl)
    signature = cxt.eval(funcName)
    # print(signature)
    full_url = targetUrl + "&_signature=" + signature

    content = requests.get(full_url).text
    print(content)


