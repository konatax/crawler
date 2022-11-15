(function(){
    console.log('c')
})();

var func = function(){
    console.log('b')
}
func();

//自调用函数不放最上面时，需要加!才不会报错,或者前面函数加分号
(function(){
    console.log('a')
})()