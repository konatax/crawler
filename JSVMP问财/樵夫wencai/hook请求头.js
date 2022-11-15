// 在js里如何进行的ajax请求
// jquery
// axios

// 原生的ajax是通过XMLHttpRequest -> 浏览器发送ajax的那个东西

// func_ = window.XMLHttpRequest.prototype.setRequestHeader;
// window.XMLHttpRequest.prototype.setRequestHeader = function(name, value){
//     if(name === 'hexin-v'){
//         debugger
//     }
//     return func_.apply(this, [name, value]);
// }
//
