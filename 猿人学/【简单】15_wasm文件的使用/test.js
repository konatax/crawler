function getM(){
    var q = instance.exports.encode;
    t1 = parseInt(Date.parse(new Date())/1000/2);
    t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
    return q(t1, t2).toString() + '|' + t1 + '|' + t2;
};

m = getM();
console.log(m);