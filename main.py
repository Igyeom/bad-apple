from PIL import Image
from pyperclip import copy
from os import listdir
import pyautogui

pyautogui.PAUSE = 1/60

l = listdir("./pngs/")
lst = []

for i in l:
    lst.append(int(l[l.index(i)][3:][:-4]))
lst.sort()

for i in lst:
    im = Image.open("./pngs/png" + str(i) + ".png")

    e = ""
    x, y = im.size

    idx = 0
    for p in im.getdata():
        idx += 1
        if p[0] < 20 and p[1] < 20 and p[2] < 20:
            e += "██"
        else:
            e += "  "
        if idx % x == 0:
            e += "\n"
    copy(e)
    pyautogui.hotkey("ctrl", "v")