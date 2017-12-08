#coding:utf-8
from selenium import webdriver
import time
import json

def do(codes):
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
				driver.find_element_by_class_name("draw-user-name").send_keys(u"韩宗稳")
				time.sleep(2)
				driver.find_element_by_class_name("draw-action").click()
				time.sleep(2)
			except Exception as e:
				print(repr(e))
		driver.quit()
	except Exception as e:
		driver.quit()
		print(repr(e))

def to_do(dict):
	codes = {}
	for k, v in dict.items():
		if (v == 0):
			print(v)
			continue
		dict[k] = 0
		codes[k] = v;
		if (len(codes) >= 2):
			try:
				do(codes)
			except Exception as e:
				print(repr(e))
			codes = {}

def printc(dict):
	c = 0
	b = 0
	for k, v in dict.items():
		if (v == 0):
			c += 1
		else:
			b += 1
	print("0: %d" % c)
	print("1: %d" % b)

if __name__ == "__main__":
	file = open('urls.txt', 'r')
	urls = file.read()
	file.close()
	dict = json.loads(urls)

	printc(dict)
	to_do(dict)

	urls = json.dumps(dict)
	file = open('urls.txt', 'w+')
	file.write(urls)
	file.close()