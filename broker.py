import requests
proxy = {
        'http': 'http://121.13.252.60'
    }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response = requests.get("http://httpbin.org/ip", headers=headers,proxies=proxy)
#response1 = requests.get("https://wallhaven.cc", proxies=proxy)
print(response.text)
response.close()