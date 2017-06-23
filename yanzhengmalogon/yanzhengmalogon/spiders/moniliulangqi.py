# -*- coding: utf-8 -*-
from selenium import webdriver
import scrapy
from scrapy.selector import Selector
from time import sleep


class MydoubanSpider(scrapy.Spider):
    name = "mydouban_moni"

    def __init__(self, ):
        super(MydoubanSpider, self).__init__()
        self.start_urls = ['https://www.douban.com/']
        self.driver = webdriver.Chrome()
        self.driver.get("https://accounts.douban.com/login")
        sleep(1)

    def parse(self, response):
        yanzhengma = raw_input('请输入验证码：')
        name = self.driver.find_element_by_xpath('//*[@id="email"]')
        name.send_keys('username用户名')
        password = self.driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys('password密码')
        key = self.driver.find_element_by_xpath('//*[@id="captcha_field"]')
        key.send_keys(yanzhengma)
        summit = self.driver.find_element_by_xpath('//*[@id="lzform"]/div[7]/input')
        summit.click()
        sleep(1)
        sel = Selector(text=self.driver.page_source)
        myname = sel.response.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]//text()').extract()
        print ''.join(myname)
        print '====================='
        pass

