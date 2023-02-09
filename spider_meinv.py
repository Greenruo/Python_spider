import os
import re
import time
import multiprocessing
import gevent
from gevent import monkey
from lxml import etree

monkey.patch_all()
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59',
    'Referer': 'https://www.2meinv.com/'
}


def get_last_page(text):
    return int(re.findall('[^/$]\d*', re.split('/', text)[-1])[0])


def image_downLoad(img_url, img_save_path, img_name):
    try:
        img_file = img_save_path + img_name
        img_data = requests.get(url=img_url, headers=headers).content
        if not os.path.exists(img_save_path):
            os.makedirs(img_save_path)
        if not os.path.exists(img_file):
            with open(img_file, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '图片下载成功！！！')
    except BaseException as e:
        print(img_url, '下载图片出错了！')


def img_req(urls, path):
    try:
        no = re.findall('[^-$][\d]', urls)[1] + re.findall('[^-$][\d]', urls)[2]
        res = requests.get(urls + ".html", headers=headers).content
        r_tree = etree.HTML(res)
        pages = r_tree.xpath('/html/body/div[2]/div/h1/span')[0].text
        last_page = get_last_page(pages)
    except BaseException as e:
        print(no, '出错了')
        return
    img_list = []
    for i in range(2, last_page + 1):
        try:
            next_url = urls + "-" + str(i) + ".html"
            print('开始解析：', next_url)
            time.sleep(1)
            _next = requests.get(next_url, headers=headers).content
            _next_html = etree.HTML(_next)
            img_url = _next_html.xpath('/html/body/div[5]/a/img/@src')[0]
            title = _next_html.xpath('/html/body/div[5]/a/img/@alt')[0]
            img_name = img_url.split("/")[-1]
            img_save_path = path + title + "/"
            img_list.append({'img_url': img_url, 'img_save_path': img_save_path, 'img_name': img_name})
        except BaseException as e:
            print(title, '图片地址解析出错了')
    g = []
    for im in img_list:
        g.append(gevent.spawn(image_downLoad, im['img_url'], im['img_save_path'], im['img_name']))
    gevent.joinall(g)
    print(no, '下载完成了！')


if __name__ == '__main__':
    save_path = "img/meinv/"
    start = 5000
    end = 2000
    process_num = 10
    while start > end:
        process = []
        for i in range(start, (start - process_num) - 1, -1):
            urls = 'https://www.2meinv.com/article-' + str(i)
            m_p = multiprocessing.Process(target=img_req, args=(urls, save_path))
            m_p.start()
            process.append(m_p)
        for k in process:
            k.join()
        start -= process_num