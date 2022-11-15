##### 爬虫时注意

paload如果是request payload,请求头要加上content-type

![1668000391529](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1668000391529.png)

这里不是，所以请求头不用加content-type

请求头顺序： ua > content-type > referer > cookie

## 什么是HOOK

本质：替换原方法

1.汇编

call   push   jump

2.js

```
//1.覆盖原函数
function xxx(){
	console.log('111');
}
xxx = function(){
	console.log('222');
}
//2.要获取原函数的值还要输出222
function xxx(){
	console.log('111');
}
//先把原方法保存
var xxx_ = xxx;
//再覆盖原方法
xxx = function() {
	console.log('222');
}
//3.覆盖浏览器环境的方法
window.alert = function() {
	console.log('?');
}

setInterval = function(){};
```

Object.defineProperty():给一个对象定义新属性，或者修改一个对象的现有属性，并返回此对象

JS逆向主要用它替换一个对象的属性

属性中储存的可能是一个方法，也有可能是一个值（值有两个方法，getter, setter)   setter就是赋值

aaa = "12345";  //触发setter 设置一个值

aaa+""              //触发getter 获取一个值

```
(function() {
	var aaa = "";  //用于接收属性
	//网站不一定先setter再getter
		Object.defineProperty(document, 'cookie', {
			//如果cookie被设置 aaa就能捕获到值
			set: function(val) {
			//想找到cookie如何生成，加一个debugger
				//debugger;
				console.log(val);
				aaa = val;
				return val;
			},
			get: function() {
				return aaa;
			}
		});
})();
```





## HOOK的时机

1.在控制台注入的hook刷新网页就失效了

让它不失效的办法

​	a.刷新网页，找到第一个加载出来的js文件，格式化，在第一行打断点，然后在控制台手动注入hook(时机可能会晚一点)

​		局限性：js文件还有html数据包中有script是异步加载，可能没办法获取到所有cookie值

​	b.利用fiddler的替换响应，注入hook

​	抓到js数据包，在第一行插入自己的hook代码，这样肯定能在加载网页js数据包前先运行自己的代码

总的来说就是  拦截=>加工=>放过

![1667207058327](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667207058327.png)

浏览器设置fiddler代理(安装proxy switchyomega插件，有设置教程)

![1667207084635](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667207084635.png)

然后直接刷新网页就能看到cookie

![1667207160086](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667207160086.png)



```
(function() {
	var aaa = "";  //用于接收属性
	//网站不一定先setter再getter
		Object.defineProperty(document, 'cookie', {
			//如果cookie被设置 aaa就能捕获到值
			set: function(val) {
			//想找到cookie如何生成，加一个debugger
				//debugger;
				//想获取某个特定cookie 可定位到获取cookie的地方
				//indexOf 如果没找到就返回-1
            if(val.indexOf("_dfp") != -1){
            	debugger;
            }
				console.log(val);
				aaa = val;
				return val;
			},
			get: function() {
				return aaa;
			}
		});
})();
```

有时候需要清空缓存

![1667221786376](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667221786376.png)

点clear site data

![1667221801293](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667221801293.png)

确保cookie是清空的





![1667227104299](C:\Users\konata\AppData\Roaming\Typora\typora-user-images\1667227104299.png)

preserve log:禁止清除缓存，每次刷新，原先的数据包不会被清空

disable cache:禁止缓存，本地调试的时候必须要勾选（有些js先缓存了就不会再请求，因此不能缓存

本地调试（本地联调）：挂代理，让所有网络请求走代理，在代理软件内拦截某些返回值，手动给他替换返回值。让计算机上的代码运行，好处是可以动态更改代码（比如可以删掉数据包中一些代码测试能不能正常运行



### 针对jsfuck

```
eval_ = eval;
eval = function (a){
    debugger;
    return eval_()
}
// 另外提供一个 Hook Function 的代码
// Function.prototype.constructor_ = Function.prototype.constructor;
// Function.prototype.constructor = function (a) {
//     debugger;
//     return Function.prototype.constructor_(a);
// };

```

```
1.hook eval
(function() { 
'use strict';
//过debuger 
var eval_ = window.eval;
window.eval = function(x){
    eval_(x.replace("debugger;","  ; "));
};
//防debuger检测
window.eval.toString = eval_.toString;
})();
2.hook debugger
//方式1
Function.prototype.constructor=function(){};
Function.prototype.constructor_bc=Function.prototype.constructor;
Function.prototype.constructor=function(){
    if (arguments==="debugger"){return}
    else{return Function.prototype.constructor_bc.apply(this,arguments)}
};
//方式2
n_eval = eval
eval = function () {
    if (argument.indexOf("debugger") === 0) {
        return
    }
    return n_eval.apply(argument)
}
//方式3
n_eval = eval
eval = function () {
    reg = RegExp(/debugger/)
    if (reg.exec(argument)) {
        return
    }
    return n_eval.apply(argument)
}
//方式4
n_Function = Function
Function = function () {
    if (argument.indexOf("debugger") === 0) {
        return
    }
    return n_Function.apply(argument)
}
//方式5
n_Function = Function
Function = function () {
    reg = RegExp(/debugger/)
    if (reg.exec(argument)) {
        return
    }
    return n_Function.apply(argument)
}
3.hook cookie
//当前版本hook工具只支持Content-Type为html的自动hook
(function () {
    'use strict';
    var cookie_cache = document.cookie;
    Object.defineProperty(document, 'cookie', {
        get: function () {
            console.log(cookie_cache);
            return cookie_cache;
        },
        set: function (val) {
            debugger;
            var cookie = val.split(";")[0];
            var ncookie = cookie.split("=");
            var flag = false;
            var cache = cookie_cache.split(";");
            cache = cache.map(function (a) {
                if (a.split("=")[0] === ncookie[0]) {
                    flag = true;
                    return cookie;
                }
                return a;
            });
            cookie_cache = cache.join(";");
            if (!flag) {
                cookie_cache += cookie + ";";
            }
        },
    });
})();
4.hook ajax
!function (t) {
    function n(e) {
        if (r[e]) return r[e].exports;
        var i = r[e] = {
            exports: {},
            id: e,
            loaded: !1
        };
        return t[e].call(i.exports, i, i.exports, n),
            i.loaded = !0,
            i.exports
    }

    var r = {};
    return n.m = t,
        n.c = r,
        n.p = "",
        n(0)
}([function (t, n, r) {
    r(1)(window)
},
    function (t, n) {
        t.exports = function (t) {
            var n = "RealXMLHttpRequest";
            t.hookAjax = function (t) {
                function r(n) {
                    return function () {
                        var r = this.hasOwnProperty(n + "_") ? this[n + "_"] : this.xhr[n],
                            e = (t[n] || {}).getter;
                        return e && e(r, this) || r
                    }
                }

                function e(n) {
                    return function (r) {
                        var e = this.xhr,
                            i = this,
                            o = t[n];
                        if ("function" == typeof o) e[n] = function () {
                            t[n](i) || r.apply(e, arguments)
                        };
                        else {
                            var u = (o || {}).setter;
                            r = u && u(r, i) || r;
                            try {
                                e[n] = r
                            } catch (t) {
                                this[n + "_"] = r
                            }
                        }
                    }
                }

                function i(n) {
                    return function () {
                        var r = [].slice.call(arguments);
                        if (!t[n] || !t[n].call(this, r, this.xhr)) return this.xhr[n].apply(this.xhr, r)
                    }
                }

                return window[n] = window[n] || XMLHttpRequest,
                    XMLHttpRequest = function () {
                        var t = new window[n];
                        for (var o in t) {
                            var u = "";
                            try {
                                u = typeof t[o]
                            } catch (t) {
                            }
                            "function" === u ? this[o] = i(o) : Object.defineProperty(this, o, {
                                get: r(o),
                                set: e(o),
                                enumerable: !0
                            })
                        }
                        this.xhr = t
                    },
                    window[n]
            },
                t.unHookAjax = function () {
                    window[n] && (XMLHttpRequest = window[n]),
                        window[n] = void 0
                },
                t.default = t
        }
    }]);
hookAjax(
    // hook functions and callbacks of XMLHttpRequest object
    {
        onreadystatechange: function (xhr) {
            //console.log("onreadystatechange called: %O", xhr)

        },
        onload: function (xhr) {
            //console.log("onload called: %O", xhr)
            xhr.responseText = "hook" + xhr.responseText;

        },
        open: function (arg, xhr) {
            console.log("open called: method:%s,url:%s,async:%s", arg[0], arg[1], arg[2], xhr);
            // arg[1] += "?hook_tag=1";
            //统一添加请求头
        },
        send: function (arg, xhr) {
            console.log("send called: %O", arg[0]);
            xhr.setRequestHeader("_custom_header_", "ajaxhook")
        },
        setRequestHeader: function (arg, xhr) {
            console.log("setRequestHeader called!", arg)
        },
        // hook attributes of XMLHttpRequest object
        timeout: {
            setter: function (v, xhr) {
                //timeout shouldn't exceed 10s
                return Math.max(v, 1000);
            }
        }
    }
);
5.防止hook检测
// 这段代码防止反hook的检测
orig = window.eval;
window.eval=function(str){debugger;orig(str);}
window.eval.toString = function (){return orig.toString();}
6.防原型链检测
//如hook了split方法
String.prototype.split_bk=String.prototype.split;
String.prototype.split = function(val){
str = this.toString()
debugger;
return str.spilt_bk(val)
}
//伪装原型链
String.prototype.split.toString=function(){
return 'function split() { [native code] }'
}
```

### HOOK请求头

```javascript

```

