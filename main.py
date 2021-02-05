from selenium import webdriver
from time import sleep
import requests

from selenium.webdriver.common.keys import Keys


def login():
    print("开始登陆")
    driver.get('http://jwxw.gzcc.cn/default2.aspx')
    driver.find_element_by_name('txtUserName').send_keys(201906120122)
    driver.find_element_by_name('TextBox2').send_keys('mavissky123')
    print("在6秒内填完验证码")
    sleep(6)
    driver.find_element_by_id('Button1').click()
    print("登陆成功")


def phase1():
    print("进入选课页面")
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4)").click()
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4) ul.sub>li:nth-of-type(1)>a").send_keys(Keys.ENTER)
    print("成功进入选课页面")


def phase2():
    print("开始选课")
    print("成功选课")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    login()
    phase1()
