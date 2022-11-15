import re
import time
import execjs
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
import asyncio

def get_ctime():
    now = time.time()
    l_time = time.localtime(now)
    # print(l_time)
    # 将时间格式化
    f_time = time.strftime("%Y-%m-%d %H:%M:%S", l_time)
    return f_time

def get_vid(play_url):
    vid = play_url.split('=')[-1]
    return vid

def get_pid():
    js_code = """
    	function createGUID() {
        return (new Date).getTime().toString(36) + '_' + Math.random().toString(36).replace(/^0./, "")
}
    """
    node = execjs.get()
    ctx = node.compile(js_code)
    ret = ctx.eval("createGUID()")
    return ret

def get_vn(play_url):
    vid = play_url.split('=')[-1]
    current_time = str(int(time.time()))
    # print('vid=',vid,type(vid))
    Vn = "|%s|%s|mg3c3b04ba|1.22.0|l8la9kso_2gd776a9qwf|4330701|https://w.yangshipin.cn/|mozilla/5.0 (windows nt |https://w.yangshipin.cn/|Mozilla|Netscape|Win32|" % (vid, current_time)
    # print('Vn=', Vn)
    return Vn

def get_qn(play_url):
    node = execjs.get()
    with open('./code.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code)
    Vn = get_vn(play_url)
    ret = ctx.eval("getQn('%s')" % Vn)
    return ret

# data是明文  获取ckey
def aes_encrypt(data):
    key = '4E2918885FD98109869D14E0231A0BF4'
    iv = '16B17E519DDD0CE5B79D7A63A4DD801C'
    key = binascii.a2b_hex(key)   #key长度必须是偶数
    iv = binascii.a2b_hex(iv)
    aes = AES.new(key=key,IV=iv,mode=AES.MODE_CBC)
    data = pad(data.encode('utf-8'), 16, style='pkcs7')
    bs = aes.encrypt(data)    #这里是字节，需要重新转为二进制数据的十六进制表示再解码 js源码要求转为字符串并大写 （tostring  upper)
    return binascii.b2a_hex(bs).decode().upper()

def get_vkey(guid, vid, ckey, pid):
    url = f"https://playvv.yangshipin.cn/playvinfo?callback=jsonp1&guid={guid}&platform=4330701&vid={vid}&defn=auto&charge=0&defaultfmt=auto&otype=json&defnpayver=1&appVer=1.22.0&sphttps=1&sphls=1&spwm=4&dtype=3&defsrc=1&encryptVer=8.1&sdtfrom=4330701&cKey={ckey}&panoramic=false&flowid={pid}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'referer': 'https://w.yangshipin.cn/'
    }
    resp = requests.get(url,headers=headers).text
    return resp
def get_vurl(vid, guid, vkey):
    vurl = f'https://mp4playcloud-cdn.ysp.cctv.cn/{vid}.YOXU10002.mp4?sdtfrom=4330701&guid={guid}&vkey={vkey}&platform=2'
    return vurl

async def play(count_url, headers, form_data):
    await asyncio.sleep(1)
    # 用协程刷播放数
    resp = requests.post(count_url, headers=headers, data=form_data)
    return resp

def call_back(future):

    return future.result()

async def main():
    play_url = 'https://w.yangshipin.cn/video?type=0&vid=y000016pug7'
    ctime = get_ctime()
    vid = get_vid(play_url)
    pid = get_pid()
    guid = 'l8la9kso_2gd776a9qwf'
    val = 2373
    # print(time.time())
    qn = str(get_qn(play_url))
    # print('qn=',qn,type(qn))
    gn = get_vn(play_url)
    data = '|' + qn + gn  # gn和Vn值是一样的
    ckey = '--01' + aes_encrypt(data)
    # print(ckey)
    vkey_resp = get_vkey(guid, vid, ckey, pid)
    # print(vkey_resp)
    vkey = re.findall(r'"fvkey":"(.*?)"', vkey_resp)[0]
    # print(vkey)
    vurl = get_vurl(vid, guid, vkey)
    # 刷播放数的url
    count_url = 'https://btrace.yangshipin.cn/kvcollect?BossId=2865'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'referer': f'https://w.yangshipin.cn/video?type=0&vid={vid}'
    }
    form_data = {
        'ctime': ctime,  # 变化
        'ua': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/105.0.0.0 safari/537.36',
        # 固定
        'hh_ua': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/105.0.0.0 safari/537.36',
        # 固定
        'platform': 4330701,  # 固定
        'guid': guid,  # 固定
        'Pwd': 1698957057,  # 固定
        'version': 'wc-1.22.0',  # 固定
        'url': f'https://w.yangshipin.cn/video?type=0&vid={vid}',  # 固定
        'hh_ref': f'https://w.yangshipin.cn/video?type=0&vid={vid}',  # 固定
        'vid': vid,  # 同一个视频固定
        'isfocustab': 1,  # 固定
        'isvisible': 1,  # 固定
        'idx': 0,  # 固定
        'val': val,  # 变化
        'pid': pid,  # 变化
        'bi': 0,  # 固定
        'bt': 0,  # 固定
        'defn': 'hd',  # 固定
        'vurl': vurl,  # vkey会变化
        'step': 6,  # 固定
        'val1': 1,  # 固定
        'val2': 1,  # 固定
        'fact1': '',  # 固定
        'fact2': '',  # 固定
        'fact3': '',  # 固定
        'fact4': '',  # 固定
        'fact5': '',  # 固定
    }
    tasks = []
    for i in range(1000):
        coroutine = play(count_url, headers, form_data)
        # 开启消息循环
        task = asyncio.create_task(coroutine)
        # task = asyncio.ensure_future(coroutine,loop=loop)
        # task.add_done_callback(call_back)
        tasks.append(task)
        # 任务函数注册到消息循环上  tasks是列表 asyncio.wait(tasks)是对象
        # asyncio.wait将任务结果收集起来，返回两个值 done（已完成的协程），spending（未完成的协程）
    return await asyncio.wait(tasks)

if __name__ == '__main__':
    # python版本高 代码如下
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 注册到异步执行对象中才会执行
    done, spending = loop.run_until_complete(main())
    for f in done:
        print(f.result())