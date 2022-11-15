// var bKB2x = window.asrsea(JSON.stringify(i6c), buU9L(["流泪", "强"]), buU9L(Rg3x.md), buU9L(["爱心", "女孩", "惊恐", "大笑"]));
// data = JSON.stringify(i6c) = '{"ids":"[1442466883]","level":"standard","encodeType":"aac","csrf_token":"8b46f61d3cc338246866723f2ce87ce2"}'
// buU9L(["流泪", "强"]) = '010001'
// buU9L(Rg3x.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
// buU9L(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'

function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}

//rsa加密
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}

//d = '{"ids":"[1442466883]","level":"standard","encodeType":"aac","csrf_token":"8b46f61d3cc338246866723f2ce87ce2"}'
//e = '010001'
//f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
//g = '0CoJUm6Qyw8W8jud'
//e f 是rsa加密的公钥私钥
function d(d, e, f, g) {
    var h = {};
    // i 实际上是随机值，直接固定一个值  encSecKey必须是配套的
    // var i = a(16);
    var i = "0J2zASPj8k68yRcH";
    var h.encText = b(d, g);
    var h.encText = b(h.encText, i);
    var h.encSecKey = '8c67f19d04950d368dc713ed0da5b5854cd7c67f423dc9b778ee62fd7dbb756260bcf42f1f760c5365a617f3e5b70263eab7523659d34b31f92eab288569bd5aafd6770a84bf7f1f23cb8afd80acbaf0db53591b2529d49168e646524b6add297b62282b9a5e6dac8220364bf92ac9e2ab9e7b7561f91b0418a70d453c50e5a1'
    // var h.encSecKey = c(i, e, f);   //将i固定以后 encSecKey的值是固定的，不用调用c也可以
    return h
}

