#百合锦簇
import tkinter
import tkinter as tk
import time
import requests
import re
from bs4 import BeautifulSoup


def click_button():
    x = int(message1.get())
    y = int(message2.get())
    for page in range(x, y):
        print(f"正在爬取第{page}页")
        imgtype = message.get()
        print(imgtype)
        url = f"http://www.netbian.com/{imgtype}/index_{page}.htm"
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

            with open('img//' + f'{imgtype}//' + name + '.jpg', mode="wb") as f:
                f.write(img_resp.content)
            print("oveer!")
            time.sleep(0.1)


#窗口界面
window = tk.Tk()
window.title('百合锦簇公众号'),window.geometry('600x245+445+400')
tk.Button(window,text='爬取',font=("宋体",40,"bold"),fg='white',bg='#76becc',relief="ridge",command=click_button).pack(expand=True, fill="both", padx=30, pady=10, side="left")
name_label1 = tk.Label(window, text='图片类型', font=('calibre', 10, 'bold'))
name_label1.pack()
message = tk.Entry(window,font=("宋体",28,"bold"),relief="ridge")
message.pack()
name_label2 = tk.Label(window, text='爬取始页', font=('calibre', 10, 'bold'))
name_label2.pack()
message1 = tk.Entry(window,font=("宋体",28,"bold"),relief="ridge")
message1.pack()
name_label3 = tk.Label(window, text='爬取末页', font=('calibre', 10, 'bold'))
name_label3.pack()
message2 = tk.Entry(window,font=("宋体",28,"bold"),relief="ridge")
message2.pack()
window.mainloop()
