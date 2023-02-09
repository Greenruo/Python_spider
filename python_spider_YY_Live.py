import requests
 
 
def page(page):
    url = 'https://api-tinyvideo-web.yy.com/home/tinyvideosv2'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    for _ in range(page+1):
        response = requests.get(url=url, headers=headers)
        data = response.json()
        #print(data)
        data_list = data['data']['data']
        #print(data_list)
        for d in data_list:
            video_title = str(d['yyNum']) + '.mp4'
            video_url = d['resurl']
 
            video_content = requests.get(url=video_url, headers=headers)
 
            with open('video\\' + video_title, mode='wb') as f:
                f.write(video_content.content)
                print('保存完成:', video_title)
 
 
if __name__ == '__main__':
    page(10)#输入请求api次数
