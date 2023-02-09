import requests
from lxml import etree
import time

url = "https://www.umei.cc/meinvtupian/meinvxiezhen/"
for x in range(2,30):#这里自行更改始末页

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}

    url2 = f"https://www.umei.cc/meinvtupian/meinvxiezhen/index_{x}.htm"

    response = requests.get(url2,headers = headers)
    response.encoding = 'utf-8'
    #print(response.text)
    tree = etree.HTML(response.text)
    list_href = tree.xpath('//*[@id="infinite_scroll"]/div[30]/div[1]/div/a/@href')#可更该代码中30部分，换成30以下的数字，这里是某页中爬取图片的开始
    #print(list_href)
    #re_list_href = reversed(list_href)

    bottom_url = list_href[0].split('/')[-1]
    url_add = url + bottom_url
    #print(url_add)
    response1 = requests.get(url_add, headers=headers)
    response1.encoding = 'utf-8'
    #print(response1.text)
    list_link = 1
    n=0
    while list_link:

        tree = etree.HTML(response1.text)
        top_name = tree.xpath('//*[@id="photos"]/h1/text()')
        #top_name = name[0].split('，')[0]
        #print(top_name[0])
        list_src = tree.xpath('/html/body/div[3]/div[2]/div[6]/a/img/@src')
        print(list_src[0])
        response_img = requests.get(list_src[0],headers)
        with open('img//'+'meinv//'+top_name[0]+str(n)+'.jpg',mode='wb') as f: #这里要创建该路径
            f.write(response_img.content)
        print("Done!",top_name[0]+str(n))
        list_link = tree.xpath('/html/body/div[3]/div[2]/div[6]/a/@href')

        bottom_url1 = list_link[0].split('/')[-1] #这里是取链接中最后的参数
        url_add1 = url + bottom_url1
        #print(url_add1)
        response1 = requests.get(url_add1, headers=headers)
        response1.encoding = 'utf-8'
        n=n + 1 #这里是图片有组图，加上不同的n命名

    response_img.close()
    response1.close()
    response.close()