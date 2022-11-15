//需要将歌单网页换成手机版才可以爬到整个歌单，否则只能爬取一首歌

function a(e, t, n) {
            var r;
            return i.setMaxDigits(131),
            r = new i.RSAKeyPair(t,"",n),
            i.encryptedString(r, e)
        }
function o(e, t) {
            var n = r.enc.Utf8.parse(t)
              , i = r.enc.Utf8.parse("0102030405060708")
              , o = r.enc.Utf8.parse(e);
            return r.AES.encrypt(o, n, {
                iv: i,
                mode: r.mode.CBC
            }).toString()
        }
// e = JSON.stringify(g) = '{"id":"2571114602","n":1000,"shareUserId":0}'
// t = (0, i.emj2code)(["流泪", "强"]) = '010001'
// n = i.BASE_CODE = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
// r = (0, i.emj2code)(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'
var U = (0, i.asrsea)('{"id":"2571114602","n":1000,"shareUserId":0}', '010001', i.BASE_CODE, '0CoJUm6Qyw8W8jud');
//    其实就是执行i.obj2query
return a.body = (0, i.obj2query)({
                        params: U.encText,
                        encSecKey: U.encSecKey
                    }),


function o(e, t) {
            var n = r.enc.Utf8.parse(t)
              , i = r.enc.Utf8.parse("0102030405060708")
              , o = r.enc.Utf8.parse(e);
            return r.AES.encrypt(o, n, {
                iv: i,
                mode: r.mode.CBC
            }).toString()
        }
//e t n r就是 var U 传进去的参数 '{"id":"2571114602","n":1000,"shareUserId":0}', '010001', i.BASE_CODE, '0CoJUm6Qyw8W8jud'
// 固定 s
    asrsea: function(e, t, n, r) {
    var i = {}
      //  s是自调用函数
      , s = function(e) {   //e是后面传入的参数16而不是上面传入的e
        var t = void 0
          , n = void 0
          , r = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          //  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          , i = "";
        for (t = 0; e > t; t += 1)
            n = Math.random() * r.length,
            n = Math.floor(n),
            i += r.charAt(n);  //盲猜 n是坐标
        return i
    }(16);
    //这里的e是'{"id":"2571114602","n":1000,"shareUserId":0}'，r是'0CoJUm6Qyw8W8jud'
    return i.encText = o(e, r),
    //    s = "AzKXLX61oO6YJf7j"
    i.encText = o(i.encText, s),
    //    s固定 encSecKey也固定 "adDE8czVTKXmWSOU"
    i.encSecKey = a(s, t, n),
    //    encSecKey = "92061bc8eb49ced2ecb96ace64d23ea2244fbd3e76673af95ae775fafca86c7518d961ddb005781a6b3a83a17a322f47557ae7ed71cc440271a50b22175bb18966b7cad465c94e559044c4e972abc80d37bbade7373edcc9b67b377c9551c6aae114d599aca513d4e5819fc6537c4fe74021492eb1baea5b0c8680f895dfd8b0"
    i
}

