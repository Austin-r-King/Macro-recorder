import pyautogui
import time
from pynput.mouse import Listener
from threading import Timer
from multiprocessing import Process

global amounttime
amounttime = int(input())

global amounttimereal
amounttimereal =amounttime

global mousepos
mousepos = []

global list
list =[]


def linstern1():
    global amounttimereal
    with Listener(on_click=on_click2) as listener1:
        Timer(amounttimereal, listener1.stop).start()
        listener1.join()


def on_click2(x, y, button, pressed):
    if pressed:
        exicuting_code()


def on_click(x, y, button, pressed):
    if pressed:
        global mousepos
        mousepos.append("Mouse clicked")
        print("Mouse clicked")


def linstern():
    global amounttime
    with Listener(on_click=on_click) as listener:
        Timer(amounttime, listener.stop).start()
        listener.join()


def actionstocode():
    global mousepos
    global list
    list = mousepos
    print (list)
    length_of_list = len(list)-1
    while (length_of_list >= 0):
        y=0
        print("code")
        x = list[length_of_list]
        print(x)
        if type(x) == float == True or type(x) == int == True:
            list[length_of_list] = time.sleep(float(x))
            y=1
        if y==0:
            if x[0] == "M":
                list[length_of_list] = pyautogui.click()
                y = 1
        if y == 0:
            if x[0] < 1000:
                list[length_of_list] = pyautogui.moveTo(list[length_of_list][0],list[length_of_list][1])
                y = 1
        if y == 0:
            if x[0] >= 1000:
                list[length_of_list] = pyautogui.moveTo(list[length_of_list][0],list[length_of_list][1])
                y = 1
        length_of_list-=1
    making_code_list()


def position():
    global amounttime
    while amounttime > 0:
        here = time.time()
        x = pyautogui.position()
        mousepos.append(x)
        print(x)
        if x == pyautogui.position():
            mousepos.append(x)
            start = time.time()
            while x == pyautogui.position():
                print("no change in mouse location")
            end = time.time()
            print(end - start)
            mousepos.append(end - start)
        x = pyautogui.position()
        mousepos.append(x)
        print(x)
        there = time.time()
        amounttime = amounttime - (there-here)
    actionstocode()


def making_code_list():
    global list
    global code
    x = 0
    for x in range(0, len(list)):
        code = lambda x: x + 1
        x += 1
    linstern1()


def exicuting_code():
    global list
    code = list
    x=0
    print("exicuting")
    while x <= len(list):
        print(code[x-1])
        x += 1


if __name__=='__main__':
    p1 = Process(target = position)
    p1.start()
    p2 = Process(target = linstern)
    p2.start()




# Ex. of printing code
#x = pyautogui.moveTo(x=0, y=0)
#x
