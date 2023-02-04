# Python_spider
# @Greenruo
①本人作为一名初学者，爬取网页仅做学习
②代码仅供参考，多有不足望指教

爬取图片之家图片
1、前言
①个人认为该网站的图片不是很好看，所以只是简单的爬取学习一下，代码简单，只爬取一页内容
②因为网页不能直接获取到源码，是通过脚本加载出来的，所以使用到了selenium、requests库，这就需要安装chrome driver

2、网站
网址：https://www.tupianzj.com/bizhi/qingchunmeinv/
![image](https://user-images.githubusercontent.com/104408603/216752319-d96ebb4b-87bb-4144-8da6-e034af14e363.png)

通过requests直接请求获得如下所示，说明网页是通过了脚本加载的
![image](https://user-images.githubusercontent.com/104408603/216752300-2f7767a3-e021-4d6d-83dc-0928ecb24171.png)

然后通过selenium获取网页源码
解析html直接提取出图片链接
最后用requests请求图片网址，下载图片并保存到项目下的img/beautiful_girl/路径，需要自己创建该路径


3、效果
![image](https://user-images.githubusercontent.com/104408603/216752329-64621da0-59a7-45c4-b77d-fe649ace36fd.png)
