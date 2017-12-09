#coding:utf-8
import re
import time
import sys
import json
import urllib.request
import urllib.parse

def geturl(url, headers={}):
	try:
		req=urllib.request.Request(url)
		for i in headers:
			req.add_header(i,headers[i])
		r=urllib.request.urlopen(req)
		html =r.read()
		return html
	except urllib.error.HTTPError as e:
	    print(e.code)
	    print(e.read().decode("utf8"))
		
def get(urls_dict, page_num, start, end):
	url="http://www.zuanke8.com/thread-%d-%d-1.html"
	#print(url)
	headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like sohow) Chrome/63.0.3239.84 Safari/537.36',
				'ContentType': 'text/html; charset=utf-8',
				'Accept-Language': 'zh-CN,zh;q=0.8',
				'Connection': 'keep-alive',
			}
	page = start
	
	while (page <= end):
		s=geturl(url % (page_num,page),headers)
		s = s.decode('gbk')
		urls=re.findall(r'http://drfhj.com/my.htm\?code=(.+?)[<"\s&]',s, re.I)
		for u in urls:
			if (len(u)>=20 and len(u) <=100):
				if (u not in urls_dict):
					urls_dict[u] = 1
			#else:
			#	print(u)
		print("page: %d" % page)
		page += 1
		time.sleep(3)
	return urls_dict

if __name__ == "__main__":
	start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
	end = int(sys.argv[2]) if len(sys.argv) > 2 else 3
	page_num = int(sys.argv[3]) if len(sys.argv) > 3 else 4536388
	urls_file_name = "urls.txt"
	try:
		try:
			open(urls_file_name).close()
		except IOError:
			open(urls_file_name,"w+").close()
		
		file = open(urls_file_name, 'r')
		urls = file.read()
		file.close()
		
		if (urls == ""):
			urls = "{}"
		urls_dict = json.loads(urls)
		print("start: %d" % len(urls_dict))
		urls_dict = get(urls_dict, page_num, start, end)
		print("end: %d" % len(urls_dict))
		urls = json.dumps(urls_dict)
		file = open(urls_file_name, 'w+')
		file.write(urls)
		file.close()
	finally:
		file.close()
	
