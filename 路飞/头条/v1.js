const jsdom = require("jsdom");  //类似于import
const {JSDOM} = jsdom;           //{JSDOM}可理解为jsdom里的一个对象

// 实例化一个对象
const resourceLoader = new jsdom.ResourceLoader({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'});

const html = '<!DOCTYPE html><p>Hello world</p>';
//人为创造浏览器
const xx = new JSDOM(html, {
    url:"https://www.toutiao.com",
    referer:"https//example.com/",
    contentType:"text/html",
    resources:resourceLoader
});

window = global    //nodejs关键字global 将window变为全局变量并且含有nodejs内置的功能   global就是当前执行的js代码中的所有全局变量
params = {
    location: {
        hash: "",
        host: "www.toutiao.com",
        hostname: "www.toutiao.com",
        href: "https://www.toutiao.com",
        origin: "https://www.toutiao.com",
        pathname: "/",
        port: "",
        protocol: "https:",
        search: "",
    },
    navigator: {
        appCodeName: "Mozilla",
        appName: "Netscape",
        appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        cookieEnabled: true,
        deviceMemory:8,
        doNotTrack: null,
        hardwareConcurrency: 4,
        language: "zh-CN",
        languages: ["zh-CN", "zh"],
        maxTouchPoints: 0,
        onLine: true,
        platform: "Win32",
        product: "Gecko",
        productSub: "20030107",
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        vendor: "Google Inc",
        vendorSub: "",
        webdriver: false
    }
};

Object.assign(window, params);
//window = global 以后，dom.window可简略不写

function xxx() {
    console.log(location.href);
    console.log(navigator.userAgent);
    // console.log(document.href);
}

xxx()

