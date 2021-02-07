import json
from selenium import webdriver
from time import sleep
import requests
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from threading import Thread

# TODO 能够实现跳转，但是现在没有选课页面，所以开始选课模块还没有完善

users = [['201906120122', 'asdasdasd123']]
courses = []
cookies = []


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
        print("手动登陆中...")
        driver.get("http://jwxw.gzcc.cn/default2.aspx")
        page_url = driver.current_url
        if page_url != "http://jwxw.gzcc.cn/default2.aspx":
            print("登录页面进不去!!!")
            return
        driver.find_element_by_name('txtUserName').clear()
        driver.find_element_by_name('txtUserName').send_keys(users[0][0])
        driver.find_element_by_name('TextBox2').clear()
        driver.find_element_by_name('TextBox2').send_keys(users[0][1])
        checkcode = input("验证码：")
        driver.find_element_by_name("txtSecretCode").send_keys(checkcode)
        driver.find_element_by_id('Button1').click()
        # 弹窗的处理
        alert_result = alert_is_present()(driver)
        if alert_result:
            print(alert_result.text)
            alert_result.accept()
        # 获取当前页url
        page_url = driver.current_url
        if page_url == "http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}":
            print("登录成功")
            cookies = driver.get_cookies()
            if cookies:
                # save_cookies
                with open("cookies.txt", "w") as fp:
                    json.dump(cookies, fp)
                print("cookie获取完毕:", cookies)
                login()
                break
            else:
                print("cookie获取失败...重新开始流程...")
        else:
            print("登录失败...重新开始流程...")
    pass


def login():
    print("进入登录页面...")
    # 先进入用户页面的网址
    driver.get("http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}")
    driver.delete_all_cookies()
    # take_cookies
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}")
    # 弹窗的处理
    alert_result = alert_is_present()(driver)
    if alert_result:
        print(alert_result.text)
        alert_result.accept()
    # 获取当前页url
    page_url = driver.current_url
    # 能不能直接进入页面
    if page_url == "http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}":
        transfer_station5()
    elif page_url == "http://jwxw.gzcc.cn/default2.aspx":
        first_login()


def transfer_station5():
    """ 中转站5 """
    print("进入选课页面...")
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4)").click()
    driver.find_element_by_css_selector(".nav>ul>li:nth-of-type(4) ul.sub>li:nth-of-type(1)>a").send_keys(Keys.ENTER)
    # 自己抢 还是 电脑抢
    qiangke(1)


def qiangke(num, ):
    """ 开始抢课 """
    print(f"开始抢课({num})...")


if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    # 如果是第一次登陆，先运行一遍 first_login()，再去运行 login()
    # first_login()
    login()
    # 非测试无需关闭
    sleep(5)
    driver.quit()
