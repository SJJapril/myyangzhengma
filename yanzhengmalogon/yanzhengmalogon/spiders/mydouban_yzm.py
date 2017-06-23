# -*- coding: utf-8 -*-
import scrapy
import urllib

class MydoubanSpider(scrapy.Spider):
    name = "mydouban_"

    def __init__(self, ):
        super(MydoubanSpider, self).__init__()
        self.start_urls = ['https://accounts.douban.com/login']
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}


    def parse(self, response):
        return [scrapy.Request("https://accounts.douban.com/login",callback=self.Login,meta={"cookiejar":1})]

    def Login(self,response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captcha) > 0:
            #人工输入验证码  下载验证码的图片
            urllib.urlretrieve(captcha[0],filename="./captcha.jpg")
            captcha_value=raw_input('查看captcha.png,有验证码请输入:')

            data={
            "form_email": "user",
            "form_password": "psaaword",
            "captcha-solution": captcha_value,
            #"redir": "https://www.douban.com/people/151968962/",      #设置需要转向的网址
            }

            return [ scrapy.FormRequest.from_response(response,headers=self.headers, meta={"cookiejar":response.meta["cookiejar"]},
              # headers=self.header,
              formdata=data, callback=self.get_content, )]
            pass

    def get_content(self,response):
        print("完成登录.........")
        test = response.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]//text()').extract()
        print ''.join(test)

