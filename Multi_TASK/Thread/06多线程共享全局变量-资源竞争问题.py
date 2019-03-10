"""共享全局变量可能产生资源竞争问题"""
import threading
import time

# 定义一个全局变量
g_num = 0


def fun1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("-----in test1 g_num = %d-----" % g_num)


def fun2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("-----in test2 g_num = %d-----" % g_num)


def main():
    t1 = threading.Thread(target=fun1, args=(1000000,))
    t2 = threading.Thread(target=fun2, args=(1000000,))

    t1.start()
    # time.sleep(1)
    t2.start()
    # 等待上面的2个线程执行完毕
    time.sleep(5)
    print("-----in main Thread g_num = %d-----" % g_num)


if __name__ == "__main__":
    main()

