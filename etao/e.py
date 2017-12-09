#coding:utf-8
from selenium import webdriver
import time
import json
import sys

def do(codes, tb_id):
	try:
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		driver = webdriver.Chrome(chrome_options=options)
		
		for code,v in codes.items():
			try:
				driver.get("http://drfhj.com/my.htm?code=%s" % (code))
				time.sleep(2)
				driver.find_element_by_class_name("act-btn-single").click()
				time.sleep(2)
				driver.find_element_by_class_name("draw-user-name").send_keys(tb_id)
				time.sleep(2)
				driver.find_element_by_class_name("draw-action").click()
				time.sleep(2)
			except Exception as e:
				print(repr(e))
		driver.quit()
	except Exception as e:
		driver.quit()
		print(repr(e))

def to_do(filename, tb_id):
	codes = {}
	count = 0
	urls_dict = get(filename)
	#tb_id = tb_id.decode()
	for k, v in urls_dict.items():
		if (v == 0):
			continue
		urls_dict[k] = 0
		codes[k] = v;
		if (len(codes) >= 2):
			try:
				do(codes, tb_id)
			except Exception as e:
				print(repr(e))
			codes = {}
		count += 1
		print ("count: %d" % count)
		save(filename, urls_dict)

def get(filename):
	try:
		file = open(filename, 'r')
		urls = file.read()
		file.close()
		urls_dict = json.loads(urls)
	except IOError:
		print("urls.txt文件不存在，请首先更新链接")
	return urls_dict
	
def save(filename,urls_dict):
	urls = json.dumps(urls_dict)
	file = open(filename, 'w+')
	file.write(urls)
	file.close()

def printc(filename):
	c = 0
	b = 0
	urls_dict = get(filename)
	for k, v in urls_dict.items():
		if (v == 0):
			c += 1
		else:
			b += 1
		#urls_dict[k] = 1
	print("已刷: %d" % c)
	print("未刷: %d" % b)

if __name__ == "__main__":
	filename = "urls.txt"
	tb_id = sys.argv[1] if len(sys.argv) > 1 else 0
	if (tb_id == 0):
		print("淘宝id错误")
	else:
		print("start: %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
		printc(filename)
		to_do(filename, tb_id)
		print("end: %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

	
