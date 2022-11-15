function S(t) {
            var e = _.a.enc.Utf8.parse("1qaz@wsx3e")
              , i = _.a.DES.decrypt({
                ciphertext: _.a.enc.Base64.parse(t)
            }, e, {
                mode: _.a.mode.ECB,
                padding: _.a.pad.Pkcs7
            });
            return i.toString(_.a.enc.Utf8)
        }
        _.a.mode.ECB = function() {
            var t = _.a.lib.BlockCipherMode.extend();
            return t.Encryptor = t.extend({
                processBlock: function(t, e) {
                    this._cipher.encryptBlock(t, e)
                }
            }),
            t.Decryptor = t.extend({
                processBlock: function(t, e) {
                    this._cipher.decryptBlock(t, e)
                }
            }),
            t
        }();
        new a["default"];
        function A() {
            var t = window.localStorage.getItem("uid");
            t && b.a.get("".concat(window.common.httpUrl, "/cutominfoapi/isToken?uid=").concat(t, "&token=").concat(window.localStorage.getItem("userToken"))).then((function(t) {
                t = JSON.parse(S(t.data));
                0 == t.data && (window.localStorage.removeItem("userToken"),
                window.localStorage.removeItem("uid"),
                window.localStorage.removeItem("username"),
                window.localStorage.removeItem("openId"),
                location.reload())
            }
            ))
        }
        function k(t) {
            return new Promise((function(e, i) {
                var a = b.a.create({
                    baseURL: common.httpUrl
                });
                a.interceptors.request.use((function(t) {
                    return A(),
                    localStorage.getItem("userToken") && (t.headers.token = localStorage.getItem("userToken")),
                    t
                }
                ), (function(t) {
                    return t
                }
                )),
                a.interceptors.response.use((function(t) {
                    return JSON.parse(S(t.data)) || t.data
                }
                ), (function(t) {
                    if (t && t.response)
                        switch (console.log(t.response.status),
                        t.response.status) {
                        case 400:
                            t.message = "请求错误";
                            break;
                        case 401:
                            t.message = "未授权的访问";
                            break
                        }
                    return t
                }
                )),
                a(t).then((function(t) {
                    e(t)
                }
                )).catch((function(t) {
                    i(t)
                }
                ))
            }
            ))
        }