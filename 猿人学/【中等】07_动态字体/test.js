success: function(data) {
    if (window.page) {} else {
        window.page = 1
    }
    ttf = data.woff;
    $('.font').text('').append('<style type="text/css">@font-face { font-family:"fonteditor";src: url(data:font/truetype;charset=utf-8;base64,' + ttf + '); }</style>');
    data = data.data;
    let html = '';
    let mad = `<tr><td><span class="ranking-li-span-1"></span></td><td><!--<img class="ranking-li-img-1"src="//ossweb-img.qq.com/images/lol/img/profileicon2/profileicon3018.jpg"alt="玩家头像">--><span class="ranking-li-span-3">九不想乖</span></td><td><span class="ranking-li-span-4"><img src="//ossweb-img.qq.com/images/lol/space/rank/2019pre/season_2019_challenger.png"alt="段位">最强王者Ⅰ</span></td><td><span class="ranking-li-span-5 fonteditor">random_rank_number</span></td><td><span class="ranking-li-span-6">random_level</span></td><td><span class="ranking-li-span-7"><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a></span></td><td><div class="m-ranking-winrate-2"><!--i的width属性等于胜率--><i class="u-ranking-winrate-i"id="ranking_4"data-win="win_rank"style="width: win_rank;"></i><a class="u-winrate ">win_rank</a><a class="u-playnumber">win_number</a></div></td></tr>`;
    let yyq = 1;
    let img_num = 1;
    let imgnum_arr = [1, 8, 3, 2, 4, 5, 7, 5, 15, 3, 9, 8, 5, 1, 3];
    let level_arr = [1, 4, 3, 2, 9, 15];
    let name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
    $.each(data, function(index, val) {
        let ppo = mad;
        for (let imgnum = 1; imgnum <= 5; imgnum++) {
            ppo = ppo.replace('img_number', yyq * window.page + imgnum_arr[imgnum])
        }
                                              //换名字
        html += ppo.replace('九不想乖', name[yyq + (window.page - 1) * 10]).replace('win_number', imgnum_arr[yyq] * level_arr[window.page] * 88 + '场').replace(/win_rank/g, imgnum_arr[yyq] + 60 + level_arr[window.page] + '%').replace('random_level', imgnum_arr[yyq] * level_arr[window.page] + 100 * level_arr[window.page]).replace('img_number', yyq * window.page).replace('random_rank_number', val.value.replace(/ /g, '') + 'LP');
        yyq += 1;
        img_num += 1
    });
    $('.append_result').text('').append(html)
},