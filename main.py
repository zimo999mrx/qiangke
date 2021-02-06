import json
from selenium import webdriver
from time import sleep
import requests
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys

# TODO 能够实现跳转，但是现在没有选课页面，所以开始选课模块还没有完善
# TODO 通过cookie跳过验证码，B站有视频
# TODO 多线程，B站有视频
file = 'cookies.json'


class alert_is_present(object):
    """ Expect an alert to be present."""
    """判断当前页面的alert弹窗"""

    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except NoAlertPresentException:
            return False


def login():
    print("开始登陆...")
    # 先进入用户页面的网址
    driver.get("http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122")
    while True:
        # 弹窗的处理
        alert_reusult = alert_is_present()(driver)
        if alert_reusult:
            print(alert_reusult.text)
            alert_reusult.accept()
        # 获取当前页url
        page_url = driver.current_url
        # 能不能直接进入页面
        if page_url == "http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122":
            phase1()
            break
        elif page_url == "http://jwxw.gzcc.cn/default2.aspx":
            print("需要手动登录...")
            driver.find_element_by_name('txtUserName').clear()
            driver.find_element_by_name('txtUserName').send_keys(201906120122)
            driver.find_element_by_name('TextBox2').clear()
            driver.find_element_by_name('TextBox2').send_keys('mavissky123')
            checkcode = input("验证码：")
            driver.find_element_by_name("txtSecretCode").send_keys(checkcode)
            driver.find_element_by_id('Button1').click()


def phase1():
    driver.refresh()
    print("进入选课页面...")
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4)").click()
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4) ul.sub>li:nth-of-type(1)>a").send_keys(Keys.ENTER)
    print("成功进入选课页面")
    phase2()


def phase2():
    print("开始选课...")
    print("成功选课")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    login()
