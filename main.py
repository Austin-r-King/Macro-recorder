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


def on_click(x, y, button, pressed):
    if pressed:
        global mousepos
        mousepos.append
        exicuting_code()


def linstern():
    global amounttime
    with Listener(on_click=on_click) as listener:
        listener.join()


def actionstocode():
    global mousepos
    global list
    list = mousepos
    length_of_list = len(list)-1
    while (length_of_list >= 0):
        x = list[length_of_list]
        print(length_of_list)
        try:
            x[0] == "M" == True
        except:
            list[length_of_list] = "time.sleep("+str(float(x))+")"
        else:
            if x[0] == "M":
                list[length_of_list] = pyautogui.click()
            elif x[0] < 1000:
                list[length_of_list] = "pyautogui.moveTo("+str(list[length_of_list][0])+","+str(list[length_of_list][1])+")"
            elif x[0] >= 1000:
                list[length_of_list] ="pyautogui.moveTo("+str(list[length_of_list][0])+","+str(list[length_of_list][1])+")"
        length_of_list-=1
    linstern()


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


def exicuting_code():
    global list
    code = list
    x=0
    print("exicuting")
    while x < len(list):
        exec(code[x])
        x += 1

position()
