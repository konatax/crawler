![图片](https://mmbiz.qpic.cn/mmbiz_gif/rDAib0gF5OjYSWh4UGpicSk6Iicic0cichnNrFdLsEM5mqbUworZBEjOn1XgiadQrpsntSIe0BlM29ClcmOh1UFJvI5Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)  

**导读**

本文主要介绍如何使用Python+OpenCV实现滑块验证码->自动拖动验证。

## 背景介绍  

前几天在某网站下载代码时，跳转到滑块验证码界面，需要验证OK后才能下载，貌似这种验证方式现在很流行，所以打算用OpenCV尝试如何让其自动拖动验证。

## 效果展示  

核心步骤是提取滑动块目标位置，如下是效果展示：

## 目标滑动块定位步骤与演示：  

实现步骤:

【1】截取验证图片，颜色通道转换为HSV，取V通道分析  

原图：  

![图片](https://mmbiz.qpic.cn/mmbiz_png/rDAib0gF5Ojb6zXOWkxaSYoOeljuJE24TxHJn1PaMUdAgmtH9R5PMvNFhHkzmt8C97PEqyRHGo5sH2ru2MGpQ0w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

V通道效果：  

![图片](https://mmbiz.qpic.cn/mmbiz_png/rDAib0gF5Ojb6zXOWkxaSYoOeljuJE24TGvQJdqhfxibkWdxrSvIHTI8ewWVXPQicrjBfRlnPovDE1X4xByaITpiag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

```
B,G,R=cv2.split(img)
```

【2】二值化 + 形态学处理

二值化效果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/rDAib0gF5Ojb6zXOWkxaSYoOeljuJE24T9l2yCgs87MIRPorWVswkmg2FjrcOdWjEibmtxaP9xicgo72nPbPzKqcQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

开运算+闭运算效果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/rDAib0gF5Ojb6zXOWkxaSYoOeljuJE24TVCVnxYIssxrlTCibdYWAjauPaicathwQyLrhcC58gHxk1oGHuaSjTic3A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

```
k1=np.ones((5,5), np.uint8)
```

【3】轮廓提取 + 宽高/面积比筛选

![图片](https://mmbiz.qpic.cn/mmbiz_png/rDAib0gF5Ojb6zXOWkxaSYoOeljuJE24T5icIB4dDMFfmIZxPLH29snW0TibRCuJpIziccFAuCKgwxtF716BO4uicow/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

其他图片测试效果(稳定性验证)：

## 自动验证完整步骤  

实现步骤:

【1】通过模板匹配定位箭头位置，作为鼠标滑动起点；  

【2】定位模板滑动块位置；

【3】控制鼠标拖动，直到与目标滑动块完全重合；

这里提供两种思路：  

① 笔者发现这个网站的起始滑动块x位置都是10，那么可以计算目标滑动块与起始滑动块X坐标差值，控制鼠标移动对应的像素量；  

② 截取目标滑动块的ROI位置，实时计算ROI被覆盖后剩余像素数量，当剩余像素数量最小时认为被覆盖完全，松开鼠标。

欢迎加入OpenCV与AI深度学习官方微信群一起学习交流：  

**源码素材与其他应用内容讨论，如有需要可加入知识星球中获取。**

更多视觉图像处理相关内容，请点击关注：OpenCV与AI深度学习。  

**觉得有用，麻烦给个赞和在看**