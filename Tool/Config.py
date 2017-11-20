#coding=utf8
from os import path
from ConfigParser import ConfigParser

class Tool_Config:
	@staticmethod
	def get(key, filename="config.ini"):
		filename = path.dirname(path.dirname(__file__)) + "/" + filename
		config = ConfigParser()
		config.read(filename)
		keys = key.split(".")
		if len(keys) > 1:
			return config.get(keys[0], keys[1])
		else:
			dt = {}
			ls = config.items(keys[0])
			for (m,n) in ls:
			    dt.setdefault(m,n)
			return dt
