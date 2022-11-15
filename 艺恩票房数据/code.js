var webDES = function() {

    var fn = function(c_a, c_b, c_c) {
        if (0x0 == c_b)
            return c_a['substr'](c_c);          //截取从c_c开始到结束的片段
        var r;
        r = '' + c_a['substr'](0x0, c_b);
        return r += c_a['substr'](c_b + c_c);
    };
    this.shell = function(data) {


            var a = parseInt(data[data.length-1], 16)+9;
            var b = parseInt(data[a]);


            data = fn(data, a, 1);

            a = data['substr'](b, 8);            //截取了8位


            data = fn(data, b, 8);

            b = _grsa_JS['enc']['Utf8']['parse'](a);   //将a转换为utf-8字节
            a = _grsa_JS['enc']['Utf8']['parse'](a);   //a与b值是相等的

            a = _grsa_JS['DES']['decrypt']({
                //将data以十六进制变为字节再转化
                'ciphertext': _grsa_JS['enc']['Hex']['parse'](data)    //将密文转换为十六进制字节
            }, b, {
                'iv': a,
                'mode': _grsa_JS['mode']['ECB'],
                'padding': _grsa_JS['pad']['Pkcs7']
            })['toString'](_grsa_JS['enc']['Utf8']);

            //                                      截取长度为 lastIndexOf('}')+1    去除}以外填充的字符 保留了json数据
            return a['substring'](0, a['lastIndexOf']('}')+1);
            //      a就是解密后的明文

            }
        }
    ;
}
  , webInstace = new webDES();
