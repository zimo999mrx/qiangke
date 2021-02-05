from selenium import webdriver
from time import sleep
import requests

from selenium.webdriver.common.keys import Keys


# TODO 需要通过cookie来跳过验证码登录
# TODO 能够实现跳转，但是现在没有选课页面，所以开始选课模块还没有完善

def login():
    print("开始登陆")
    # 先进入用户页面的网址
    driver.get("http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122")
    # 获取当前页url
    pageUrl = driver.current_url
    # 判断能不能cookie在不在，不在进不去用户页面
    if pageUrl == "http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122":
        print("之前已登陆")
        phase1()
    elif pageUrl == "http://jwxw.gzcc.cn/default2.aspx":
        print("需要手动登录")
        driver.get('http://jwxw.gzcc.cn/default2.aspx')
        driver.find_element_by_name('txtUserName').send_keys(201906120122)
        driver.find_element_by_name('TextBox2').send_keys('mavissky123')
        print("在6秒内填完验证码")
        sleep(6)
        driver.find_element_by_id('Button1').click()
        print("登陆成功")
        phase1()
    else:
        print("出现未知问题")


def phase1():
    print("进入选课页面")
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4)").click()
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4) ul.sub>li:nth-of-type(1)>a").send_keys(Keys.ENTER)
    print("成功进入选课页面")
    phase2()


def phase2():
    print("开始选课")
    print("成功选课")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    login()
