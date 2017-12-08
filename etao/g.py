#coding:utf-8
import re
import time
import json
import urllib.request
import urllib.parse

def geturl(url, headers={}):
	try:
		req=urllib.request.Request(url)
		#设置headers
		for i in headers:
			req.add_header(i,headers[i])
		r=urllib.request.urlopen(req)
		html =r.read()
		return html
	except urllib.error.HTTPError as e:
	    print(e.code)
	    print(e.read().decode("utf8"))
		
def get(dict):
	url="http://www.zuanke8.com/thread-4536388-%d-1.html"
	headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
				'ContentType': 'text/html; charset=utf-8',
				'Accept-Language': 'zh-CN,zh;q=0.8',
				'Connection': 'keep-alive',
			}
	page = 0
	
	while (page < 3):
		s=geturl(url % (page),headers)
		#s = '''http://drfhj.com/my.htm?code=sdaaaaaaaasddd01"http://drfhj.com/my.htm?code=sdaaaaaaaasddd02"http://drfhj.com/my.htm?code=sdaaaaaaaasddd03 http://drfhj.com/my.htm?code=sdaaaaaaaasddd04<'''
		s = s.decode('gbk')
		urls=re.findall(r'http://drfhj.com/my.htm\?code=(.+?)[<"\s&]',s, re.I)
		for u in urls:
			if (len(u)>=20 and len(u) <=100):
				if (u not in dict):
					dict[u] = 1
			else:
				print(u)
		page += 1
		time.sleep(5)
	return dict

if __name__ == "__main__":
	try:
		file = open('urls.txt', 'r')
		urls = file.read()
		file.close()
		print(urls)
		if (urls == ""):
			urls = "{}"
		dict = json.loads(urls)
		print(len(dict))
		dict = get(dict)
		print(len(dict))
		urls = json.dumps(dict)
		file = open('urls.txt', 'w+')
		file.write(urls)
		file.close()
	finally:
		file.close()
	