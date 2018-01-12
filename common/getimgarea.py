# -*- coding: utf-8 -*-

# @Author  : wyq
# @Time    : 2018/1/12 13:39
# @desc    :
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshotForArea.png')
    os.system('adb pull /sdcard/screenshotForArea.png .')
def on_click(event):
    ix, iy = event.xdata, event.ydata
    coords = [(ix, iy)]
    print ("x,y : ", coords)
def show():
    fig = plt.figure()
    pull_screenshot()
    img = np.array(Image.open('screenshotForArea.png'))
    im = plt.imshow(img, animated=True)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

if __name__ == '__main__':
    show()

