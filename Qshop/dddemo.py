# import logging
# logging_header = logging.FileHandler("test.log",encoding="utf-8")
# stream_header = logging.StreamHandler()
# log_format = "%(asctime)s【%(levelname)s】%(message)s"
# time_format = "%Y-%m-%d %H:%M:%S"
# logging.basicConfig(level=logging.DEBUG,format=log_format,datefmt=time_format)
# [logging_header,stream_header]
# logging.debug("这是个debug信息")
# logging.info("这是个info信息")
# logging.warning("这是个warning信息")
# logging.error("这是一个error信息")
# logging.critical("这是一个critical信息")

from selenium import webdriver
chrome1 = webdriver.Firefox()
chrome1.get("https://www.baidu.com/")

class Payorde:
    order_number = 1
    order_data = 2
    order_total = 1
    def n(self):
        return (order_number+order_data)
