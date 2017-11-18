#coding:utf-8
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys  

class Jd:
	__driver = None
	__headless = True
	__display = None
	
	def __init__(self, headless=True):
		if headless == True:
			self.__display = Display(visible=0, size=(1366,768))
			self.__display.start()
		self.__headless = headless
		options = webdriver.ChromeOptions()
        	options.add_argument("--no-sandbox")
	        self.__driver = webdriver.Chrome(chrome_options=options)

	def __del__(self):
		self.__driver.quit()
		if self.__headless == True:
                        self.__display.stop()

	def login(self, name, passwd):
		self.__driver.get('https://passport.jd.com/uc/login')
		time.sleep(3)
		self.__driver.find_element_by_link_text("账户登录").click()
		time.sleep(1)
		self.__driver.find_element_by_id("loginname").send_keys(name)
		time.sleep(1)
		self.__driver.find_element_by_id("nloginpwd").send_keys(passwd)
		time.sleep(1)
		self.__driver.find_element_by_id("nloginpwd").send_keys(Keys.ENTER)
		time.sleep(3)

	def sign(self):
		self.__driver.get("http://vip.jd.com/home.html")
		time.sleep(3)
		self.__driver.find_element_by_id("signIn").click()

if __name__ == "__main__":
	jd = Jd()
	jd.login("username", "password")
	jd.sign()
	del jd
