#coding:utf-8
import sys
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
	def __del__(self):
		if self.__headless == True:
			self.__display.stop()
			self.__driver.quit()

	def login(self, name, passwd):
		self.__driver.get('https://passport.baidu.com/v2/')
		time.sleep(3)
		self.__driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(name)
		time.sleep(1)
		self.__driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys(passwd)
		time.sleep(1)
		self.__driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys(Keys.ENTER)
		return;

		self.__driver.find_element_by_link_text("亲，请登录").click()
#		self.__driver.get('https://login.taobao.com/member/login.jhtml')
		time.sleep(3)
		ele_login = self.__driver.find_element_by_class_name("login-switch")
		ActionChains(self.__driver).move_to_element(ele_login).click().perform()
#		self.__driver.save_screenshot("/usr/local/www/sohow/html/static/t1.png")
		time.sleep(1)


		ele_username = self.__driver.find_element_by_id("TPL_username_1")
		ele_password = self.__driver.find_element_by_id("TPL_password_1")
		ele_username.clear()
		ele_password.clear()
	
		ActionChains(self.__driver).move_to_element(ele_username).click().perform()
		time.sleep(1)
		ele_username.send_keys(name)
		time.sleep(1)
		ActionChains(self.__driver).move_to_element(ele_password).click().perform()
		time.sleep(1)
		ele_password.send_keys(passwd)
		time.sleep(1)
		#self.__driver.find_element_by_id("TPL_password_1").send_keys(Keys.ENTER)

		ele_hua = self.__driver.find_element_by_id("nc_1_n1z")

		actions = ActionChains(self.__driver)
		actions.move_to_element(ele_hua)
		actions.click_and_hold(ele_hua)
		actions.pause(1)

		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)
		actions.move_by_offset(30, 0)
		actions.pause(1)

		actions.perform()
		#ActionChains(self.__driver).move_to_element(ele_hua).drag_and_drop_by_offset(ele_hua,300,0).perform()
		time.sleep(2)

		ele_submit = self.__driver.find_element_by_id("J_SubmitStatic")
		ActionChains(self.__driver).move_to_element(ele_submit).click().perform()
		time.sleep(3)
#		self.__driver.save_screenshot("/usr/local/www/sohow/html/static/t.png")
	def sign(self):
		self.__driver.get("https://taojinbi.taobao.com/index.htm")
		time.sleep(3)
		print self.__driver.title
		self.__driver.find_element_by_link_text("今日可领").click()

if __name__ == "__main__":
	headless = False if len(sys.argv) > 1 and sys.argv[1] == "show" else True
	conf = Tool_Config.get("bd")
	tb = Tb(headless)
	try:
		tb.login(conf["username"], conf["password"])
		#tb.sign()
	except:
		print "except"
	if headless == True:
		del tb
