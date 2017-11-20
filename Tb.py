#coding:utf-8
from Tool.Config import Tool_Config
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains

class Tb:
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
        	options.add_argument("--start-maximized")
	        self.__driver = webdriver.Chrome(chrome_options=options)
		self.__driver.viewportSize={'width':1366,'height':768}
	def __del__(self):
		self.__driver.quit()
		if self.__headless == True:
                        self.__display.stop()

	def login(self, name, passwd):
		self.__driver.get('https://login.taobao.com/member/login.jhtml')
		time.sleep(3)
		ele_login = self.__driver.find_element_by_class_name("login-switch")
		ActionChains(self.__driver).move_to_element(ele_login).click().perform()
		self.__driver.save_screenshot("/usr/local/www/sohow/html/static/t1.png")
		time.sleep(1)		
		self.__driver.find_element_by_id("TPL_username_1").send_keys(name)
		time.sleep(1)
		self.__driver.find_element_by_id("TPL_password_1").send_keys(passwd)
		time.sleep(1)
		self.__driver.find_element_by_id("TPL_password_1").send_keys(Keys.ENTER)
		time.sleep(3)
		self.__driver.save_screenshot("/usr/local/www/sohow/html/static/t.png")
	def sign(self):
		self.__driver.get("https://taojinbi.taobao.com/index.htm")
		time.sleep(3)
		print self.__driver.title
		self.__driver.find_element_by_link_text("今日可领").click()

if __name__ == "__main__":
	conf = Tool_Config.get("tb")
	print conf
	tb = Tb()
#	try:
	tb.login(conf["username"], conf["password"])
	#	tb.sign()
#	except:
	#	print "except"
	del tb
