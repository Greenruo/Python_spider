import time
import requests
import re
from bs4 import BeautifulSoup

for page in range(1, 10):
    print(f"正在爬取第{page}页")
    url = f"http://www.netbian.com/dongman/index_{page}.htm"
    resp = requests.get(url)
    print(resp)
    resp.encoding = 'gbk'
    resp1 = resp.text
    # print(resp1)
    obj = re.compile(r'<a href="/desk/(?P<id>.*?).htm" title="(?P<name>.*?)" target', re.S)
    alist = obj.finditer(resp1)
    for a in alist:
        id = a.group("id")
        name = a.group("name")
        # print(id,name)
        url = f'http://www.netbian.com/desk/{id}-1920x1080.htm'
        # print(url)
        img_resp = requests.get(url)
        # print(img_resp.text)
        img_resp_text = img_resp.text
        # print(img_resp_text)
        child_page = BeautifulSoup(img_resp_text, "html.parser")
        p = child_page.find("td", align="left")
        img = p.find("img")
        src = img.get("src")
        img_resp = requests.get(src)
        ''''''
        obj1 = re.compile(r'<tr><td align="left">.*？"(?P<Url>.*?)" title', re.S)
        url2 = obj1.findall(img_resp_text)
        # print(url2)

        with open('img//' + 'dongman//' + name + '.jpg', mode="wb") as f:
            f.write(img_resp.content)
        print("oveer!")
        time.sleep(0.1)