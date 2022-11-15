import re
import json
import base64
import pymysql
import requests
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def decrypt_data(data):
    # 公钥长度超过8位，只需要取前面八位就可以
    key = "1qaz@wsx3e"
    key = key[:8].encode('utf-8')
    # print('key:',key)
    # ciphertext: _.a.enc.Base64.parse(t)
    # js源码中有写，密文经过base64处理   将普通字符串变为字节（解密时必须将密文变为字节） 是b64decode()
    # 将字节变为base64格式字节 b64encode()
    data = base64.b64decode(data)
    print('data:',data)
    data = pad(data, block_size=16, style='pkcs7')
    des = DES.new(key=key,mode=DES.MODE_ECB)
    bs = des.decrypt(data)
    # 可能因为密文解密之前有填充过，因此出现一些无法decode的字符，需要加上'ignore'
    # print('bs:',bs.decode('utf-8','ignore'))
    return bs.decode('utf-8','ignore')

def to_sql(data):
    # 存到mysql  mytestdb数据库中 ctbpsp表中
    conn = pymysql.connect(host='localhost',user='root',password='root',database='mytestdb')
    cursor = conn.cursor()
    sql = """
        insert into ctbpsp(project_name,notice_name,notice_media,bulletin_type_name,regin_province,server_plat,trade_plat,region_code,region_name,notice_send_time,notice_url,supervise_dept_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    result = cursor.executemany(sql, data)
    conn.commit()
    print(result)

    cursor.close()
    conn.close()

def get_resp(num):
    url = 'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/%d' % (num)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers).text
    return resp

def main():
    num = int(input('请输入想要爬取的页数：'))
    for n in range(num):
        resp = get_resp(n+1)
        result = decrypt_data(resp)
        # 由于密文在解密之前有填充，所以后面需要去掉不需要的数据，最后面的}以外的字符串需要去掉
        r = re.match(r'\{.*\}', result)
        d = json.loads(r.group())
        l = d['data']['dataList']
        rr = []
        for i in range(len(l)):
            project_name = l[i]['tenderProjectName']
            notice_name = l[i]['noticeName']
            notice_media = l[i]['noticeMedia']
            bulletin_type_name = l[i]['bulletinTypeName']
            regin_province = l[i]['reginProvince']
            server_plat = l[i]['serverPlat']
            trade_plat = l[i]['tradePlat']
            region_code = l[i]['regionCode']
            region_name = l[i]['regionName']
            notice_send_time = l[i]['noticeSendTime']
            notice_url = l[i]['noticeUrl']
            supervise_dept_name = l[i]['superviseDeptName']
            rr.append([project_name, notice_name, notice_media, bulletin_type_name, regin_province, server_plat, trade_plat, region_code, region_name, notice_send_time, notice_url,supervise_dept_name])
        to_sql(rr)

if __name__ == '__main__':
    # main()
    data = "gQHO7zwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyelZhU01McHlhMFAxaUhxNjF6Y28AAgSjE0ZjAwQIBwAA"
    key = "1qaz@wsx3e"
    key = key[:8].encode('utf-8')
    # print('key:',key)
    # ciphertext: _.a.enc.Base64.parse(t)
    # js源码中有写，密文经过base64处理   将普通字符变为字节（解密时必须将密文解码为字节） 是b64decode()
    # 将字节变为base64格式字节 b64encode() 把杂乱无章的字节处理成base64字符串才方便传输（也是b开头 然后再.decode('utf-8')就把b去掉了
    data = base64.b64decode(data)
    # print('data:', data)
    data = pad(data, block_size=16, style='pkcs7')
    des = DES.new(key=key, mode=DES.MODE_ECB)
    bs = des.decrypt(data)
    # 可能因为密文解密之前有填充过，因此出现一些无法decode的字符，需要加上'ignore'
    #也可导入from Crypto.Utils.Padding import unpad
    # bs = unpad(bs, 16)
    # print('bs:',bs.decode('utf-8','ignore'))
    print(bs.decode('utf-8', 'ignore'))


