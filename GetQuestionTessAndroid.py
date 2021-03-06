# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/8 20:38
# @desc    : 答题闯关辅助，截屏 ，OCR 识别，百度搜索


from PIL import Image
from common import screenshot, ocr, methods
# from common import getimgarea
# from threading import Thread
import time
# python3默认utf-8编码，python2x需要用以下三句防止乱码
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 调试得到区域坐标 （功能：屏幕截图并打开，显示鼠标所处屏幕坐标，点击print 横纵坐标，用于方便确定问题及选项区域）
# getimgarea.show() #运行时请注释该方法
# exit()
while True:
    # t1 = time.clock()
    # 截图
    screenshot.check_screenshot()

    img = Image.open("./screenshot.png")

    # 文字识别
    question, choices = ocr.ocr_img(img)
    # print(question)
    # exit()
    # t2 = time.clock()
    # 用不同方法输出结果，取消某个方法在前面加上#

    # # 打开浏览器方法搜索问题
    # methods.run_algorithm(0, question, choices)
    # # 用选项在问题页面中计数出现词频方法
    methods.run_algorithm(2, question, choices)
    # # 将问题与选项一起搜索方法，并获取搜索到的结果数目
    methods.run_algorithm(1, question, choices)

    # 多线程
    # m1 = Thread(methods.run_algorithm(0, question, choices))
    # m2 = Thread(methods.run_algorithm(1, question, choices)) # 推荐方式2
    # m3 = Thread(methods.run_algorithm(2, question, choices))
    # m1.start()
    # m2.start()
    # m3.start()

    # end_time = time.clock()
    # print("t2 - t1:")
    # print(t2 - t1)
    # print("\nendtime - t2:")
    # print(end_time - t1)
    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break
    print('------------------------')
