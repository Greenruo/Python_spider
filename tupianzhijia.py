import requests
from lxml import etree
import time


url = "https://www.tupianzj.com/meinv/xiezhen/list_179_2.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
response = requests.get(url,headers = headers)
response.encoding = 'utf-8'
print(response.text)

'''tree = etree.HTML(response.text)
list_href = tree.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div/div/div[1]/div/a/@href')
#print(len(list_src))
#re_list_href = reversed(list_href)
for i in list_href:
    n = 0
    #print(i)
    bottom_url=i.split('/')[-1]
    url_add = url+bottom_url
    print(url_add)
    response1 = requests.get(url_add,headers = headers)
    response1.encoding = 'utf-8'
    #print(response.text)
    tree1 = etree.HTML(response1.text)
    name = tree1.xpath('/html/body/div[3]/div[2]/div[5]/h3/text()')
    top_name = name[0].split('，')[0]
    print(top_name)


    list_src= tree1.xpath('/html/body/div[3]/div[2]/div[6]/a/img/@src')
    print(list_src[0])
    response2_img = requests.get(list_src[0],headers)
    with open('img//'+'meinv//'+top_name+str(n)+'.jpg',mode='wb') as f:
        f.write(response2_img.content)


    list_link_href = tree1.xpath('/html/body/div[3]/div[2]/div[6]/a/@href')
    bottom_url2 = list_link_href[0].split('/')[-1]
    href_url = url + bottom_url2
    response3 = requests.get(href_url, headers)
    
    with open('img//' + 'meinv//' + top_name + str(n) + '.jpg', mode='wb') as f:
        f.write(response3_img.content)
    n = n + 1

        response3_1 = requests.get(img_url, headers)
        tree3 = etree.HTML(response3_1.text)
        list_link3 = tree3.xpath('/html/body/div[3]/div[2]/div[6]/a/img/@src')
        response3_img = requests.get(list_link3[0], headers)

    """
    #print(list_link)
    for j in list_link:
        bottom_url2 = url
    if list_link[0]:
        url_add2 = url + list_link[0]
        print(url_add2)"""
response.close()'''