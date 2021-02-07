import json
from selenium import webdriver
from time import sleep
import requests
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from threading import Thread

# TODO 能够实现跳转，但是现在没有选课页面，所以开始选课模块还没有完善

users = [['201906120122', 'asdasdasd123']]


class alert_is_present(object):
    """ 判断当前页面的alert弹窗 """

    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except NoAlertPresentException:
            return False


def first_login():
    """ 第一次登陆，手动登录获取cookie """
    while True:
        # 弹窗的处理
        alert_result = alert_is_present()(driver)
        if alert_result:
            print("系统弹窗了：", alert_result.text)
            alert_result.accept()
        # 获取当前页url
        page_url = driver.current_url
        #
        print("手动登陆中...")
        driver.get("http://jwxw.gzcc.cn/default2.aspx")
        driver.find_element_by_name('txtUserName').clear()
        driver.find_element_by_name('txtUserName').send_keys(users[0][0])
        driver.find_element_by_name('TextBox2').clear()
        driver.find_element_by_name('TextBox2').send_keys(users[0][1])
        checkcode = input("验证码：")
        driver.find_element_by_name("txtSecretCode").send_keys(checkcode)
        driver.find_element_by_id('Button1').click()
        sleep(0.5)
        page_url = driver.current_url
        if page_url == "http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}":
            print("登录成功")
            cookies = driver.get_cookies()
            if cookies:
                print("cookie获取完毕:", cookies)
                # 下一步
                break
            else:
                print("cookie获取失败...重新开始流程...")
        else:
            print("登录失败...重新开始流程...")
    pass


def transition_login_to_course_selection():
    """ 从登录页面过渡到选课页面 """
    driver.refresh()
    print("进入选课页面...")
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4)").click()
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4) ul.sub>li:nth-of-type(1)>a").send_keys(Keys.ENTER)
    course_selection()


def course_selection():
    """ 具体的选课业务 """
    print("开始选课...")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    first_login()
