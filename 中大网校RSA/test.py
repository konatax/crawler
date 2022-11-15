import requests
import json
import time
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
import urllib, sys
import ssl
from Crypto.Util.Padding import pad

def base64_api(img):
    data = {"username": 'q6035945', "password": 'q6035945', "typeid": 3, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

# 加密  s是输入的密码+''+getTime返回的data
# 流程：输入文本（str）→字符串编码（默认utf-8）（bytes）→rsa加密（bytes）→base64编码（bytes）→解码为字符串（str）
def enc(s):
    key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
    # 加载密钥
    # 因为前端的rsa是将base64封装到里面了, python的rsa加密不经过base64处理的话 是 字节串,字节串不利于传输所以需要转成base64.
    # base64.b64decode(key)将key（base64形式的字符串）进行base64解码得到二进制形式的字符串 就是把引号里面的字母换成二进制形式
    # 如果是自己文件读取的公钥（mode='rb') 就不需要转码
    rsa_key = RSA.importKey(base64.b64decode(key))
    rsa_new = PKCS1_v1_5.new(rsa_key)
    # 将密码转换为字节再加密 加密以后依然是字节
    mi = rsa_new.encrypt(s.encode('utf-8'))
    # 编码为base64字节再解码成字符串
    return base64.b64encode(mi).decode('utf-8')

def main():

    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Referer': 'https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    # 这里是浏览器地址栏的网址而不是request url
    login_url = 'https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F'
#     进入登录页加载到cookie
    session.get(login_url)
    time.sleep(1)
    resp = session.post('https://user.wangxiao.cn/apis//common/getImageCaptcha').json()
    img = resp["data"].split(',')[1]
    # print(base64Code)
    # 识别的验证码
    verify_code = base64_api(img)
    print(verify_code)
    get_time_resp = session.post("https://user.wangxiao.cn/apis//common/getTime").json()
    get_time = get_time_resp['data']
    print(get_time,type(get_time))
    #登录流程
    login_verify_url = "https://user.wangxiao.cn/apis//login/passwordLogin"
    username = '13672684677'
    password = enc('85225387luluxiu'+get_time)
    print(password)
    data = {
        "imageCaptchaCode": verify_code,
        "password": password,
        # 注意这里的大小写
        "userName": username
    }
    res = session.post(login_verify_url, data=json.dumps(data)).json()
    print(res)

#登陆成功后的cookie处理
    session.cookies["autoLogin"] = "true"
    session.cookies["userInfo"] = json.dumps(res["data"])
    session.cookies["token"] = res["data"]["token"]
    session.cookies["UserCookieName"] = res["data"]["userName"]
    session.cookies["OldUsername2"] = res["data"]["userNameCookies"]
    session.cookies["OldUsername"] = res["data"]["userNameCookies"]
    session.cookies["OldPassword"] = res["data"]["passwordCookies"]
    session.cookies["UserCookieName_"] = res["data"]["userName"]
    session.cookies["OldUsername2_"] = res["data"]["userNameCookies"]
    session.cookies["OldUsername_"] = res["data"]["userNameCookies"]
    session.cookies["OldPassword_"] = res["data"]["passwordCookies"]
    session.cookies[res["data"]["userName"] + "_exam"] = res["data"]["sign"]
    q_url = "https://ks.wangxiao.cn/practice/listQuestions"
    #subsign在html中，表示科目  https://ks.wangxiao.cn/TestPaper/list?sign=jijin  top 代表前面多少题数，默认30
    d = {
            "examPointType":"",
            "practiceType":"2",
            "questionType":"",
            "sign":"jijin",
            "subsign":"8a8e2341203868bef5af",
            "top":"289",
    }
    r = session.post(q_url,data=json.dumps(d))
    print(r.text)


if __name__ == '__main__':
    # pw = enc('123456')
    # print(pw)
    # s = b'abc'
    # ss = base64.b64encode(s)
    # print(ss)               #b'YWJj'
    # sss = base64.b64decode(ss)
    # print(sss)              #b'abc'
    # print(sss.decode('utf-8'))   #abc
    # data = "data:image/png;base64,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"
    # d = data.split(',')
    # print(d)
    # base64_api()
    main()