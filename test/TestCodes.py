def test1():
    no = 201906120122
    str1 = "http://jwxw.gzcc.cn/xs_main.aspx?xh=" + f"{no}"
    if "http://jwxw.gzcc.cn/xs_main.aspx?xh=201906120122" == str1:
        print("yes")
    else:
        print("no")
        print(f"{str1}")


def test2():
    print("1")
    return
    l = []
    if not l:
        print("1")
    else:
        print(l)


if __name__ == '__main__':
    test2()
