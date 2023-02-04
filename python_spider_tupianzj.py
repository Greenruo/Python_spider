import requests
from selenium import webdriver
from lxml import etree
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
web = webdriver.Chrome(chrome_options=option) # don't open webdriver

web.get('https://www.tupianzj.com/bizhi/qingchunmeinv/')
#获取网页代码
element = web.page_source
#print(web.title,element)

html = etree.HTML(element)
list = html.xpath('//*[@id="container"]/div/div/div[3]/div/ul/li/a/img/@src')
print(list)
n = 1
for i in list:
    response_img = requests.get(i)
    list_name = html.xpath(f'//*[@id="container"]/div/div/div[3]/div/ul/li[{n}]/a/label/text()')
    print(list_name)

    with open("img//"+"beautiful_girl//"+list_name[0]+".jpg",mode='wb') as f:
        f.write(response_img.content)

    print("Done!",list_name[0],n)
    n = n + 1
    time.sleep(1)
web.quit()
