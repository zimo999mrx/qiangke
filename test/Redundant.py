def start_threading():
    """ 多线程打开以下事件 """
    print("多线程准备...")
    threads = []
    # 线程数
    nloops = range(9)
    # 线程对象放入列表
    for i in nloops:
        t = Thread(target=login, args=(i,))
        threads.append(t)
    # 开始进程
    for i in nloops:
        threads[i].start()
    # join
    for i in nloops:
        threads[i].join()
    print("多线程-end")


def second_login(cookies):
    driver.get("https://www.baidu.com/")
    driver.delete_all_cookies()
    print("1")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    sleep(0.5)
    page_url = "http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{users[0][0]}"
    driver.get(page_url)
    pass


def test_threadins(cookies):
    t1 = Thread(target=second_login, args=(cookies,))
    t2 = Thread(target=second_login, args=(cookies,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    sleep(12)
    driver.quit()
    pass


def login():
    """ 登录操作 """
    print("开始登陆...")
    # 先进入用户页面的网址
    driver.get("http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122")
    while True:
        # 弹窗的处理
        alert_result = alert_is_present()(driver)
        if alert_result:
            print(alert_result.text)
            alert_result.accept()
        # 获取当前页url
        page_url = driver.current_url
        # 能不能直接进入页面
        if page_url == "http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122":
            transition_login_to_course_selection()
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
            # print("获取cookie...")
