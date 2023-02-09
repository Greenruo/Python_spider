import requests
from lxml import etree
import time
url = "https://desk.3gbizhi.com/deskDM/"
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
response = requests.get(url=url,headers=headers1)
#print(response.text)
tree = etree.HTML(response.text)
list = tree.xpath("/html/body/div[5]/ul/li/a/@href")

for i in list:
    print(i)
    response1 = requests.get(i)
    tree1 = etree.HTML(response1.text)
    id = tree1.xpath("/html/body/div[3]/h2/text()")
    url_source = tree1.xpath("/html/body/div[3]/div[2]/a/@href")#/html/body/div[3]/div[2]/a
    #print(id[0],url_source)
    url1 = url_source[0]
    #print(url1)
    img_source = requests.get(url1)
    #下载

    with open('img//' + '3G_dongman_wp//' + id[0] + '.jpg', mode="wb") as f:
        f.write(img_source.content)
    print("oveer!")
    time.sleep(0.1)
response1.close()
response.close()
