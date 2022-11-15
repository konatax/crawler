let paramss = {
      url: '/common/getTime',
    }
//ress:{code: 0, msg: null, data: '1664260344651', operation_date: '2022-09-27 14:32:24'}
//ress的数据是从getTime请求得到的
zdAjax(paramss, (ress) => {
      var param = {
        url: '/login/passwordLogin',
        data: {
          userName: username,
          password: encryptFn(pwd + '' + ress.data),
          imageCaptchaCode: imgCode,
        },
        //进入encryptFn()函数
 window.encryptFn = function(e) {
            var o = new JSEncrypt;
            return o.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"),
            o.encrypt(e)
        }

//有公钥，必定是RSA加密
//用RAS库就能解决
//        这段代码可知密码加密以后需要经过base64编码
JSEncrypt.prototype.encrypt = function(a) {
        try {
            return hex2b64(this.getKey().encrypt(a))
        } catch (b) {
            return !1
        }


         JSEncrypt.prototype.setPublicKey = function(a) {
        this.setKey(a)
    }
    JSEncrypt.prototype.setKey = function(a) {
        this.log && this.key && console.warn("A key was already set, overriding existing."),
        this.key = new JSEncryptRSAKey(a)
    }
    var JSEncryptRSAKey = function(a) {
        RSAKey.call(this),
        a && ("string" == typeof a ? this.parseKey(a) : (this.hasPrivateKeyProperty(a) || this.hasPublicKeyProperty(a)) && this.parsePropertiesFrom(a))
    };