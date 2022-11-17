import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB'
rsa_key = RSA.importKey(base64.b64decode(key))   #转换成字节
rsa = PKCS1_v1_5.new(rsa_key)
username = rsa.encrypt('13672684688'.encode('utf-8'))
print(base64.b64encode(username).decode('utf-8'))  #和网站加密结果不一样,网站加密都是小写字母