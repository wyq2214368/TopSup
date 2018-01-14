# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 19:34
# @desc    :

from PIL import Image
import pytesseract
from PIL import ImageFilter

# 二值化算法
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


# 去除干扰线算法
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

def ocr_img(image):

    # 切割题目和选项位置，左上角坐标和右下角坐标,自行测试分辨率
    # 5.7 英寸（锤子m1）
    # question_im = image.crop((120, 400, 1330, 700))
    # choices_im = image.crop((170, 760, 1330, 1422))
    # 坚果 pro1 ( 5.5 英寸)
    # question_im = image.crop((50, 350, 1000, 560))
    # choices_im = image.crop((75, 535, 990, 1150))
    # question = img.crop((75, 315, 1167, 789)) # iPhone 7P( 5.5 英寸 )
    # 冲顶大会 (华为v9   5.7英寸)
    # question_im = image.crop((50, 438, 1342, 722))
    # choices_im = image.crop((50, 722, 1246, 1360))
    # 西瓜视频（华为v9 — 5.7 英寸）
    question_im = image.crop((100, 500, 1312, 805))
    choices_im = image.crop((100, 820, 1200, 1670))
    # 百万赢家 （华为v9  5.7英寸)
    # question_im = image.crop((75, 542, 1300, 882))
    # choices_im = image.crop((75, 868, 1260, 1620))
    #芝士超人
    # question_im = image.crop((46, 456, 1358, 756))
    # choices_im = image.crop((30, 770, 1270, 1528))

    # 边缘增强滤波,不一定适用
    #question_im = question_im.filter(ImageFilter.EDGE_ENHANCE)
    #choices_im = choices_im.filter(ImageFilter.EDGE_ENHANCE)

    # 转化为灰度图
    question_im = question_im.convert('L')
    choices_im = choices_im.convert('L')
    # 把图片变成二值图像
    question_im = binarizing(question_im, 190)
    choices_im = binarizing(choices_im, 190)
    #img=depoint(choices_im)
    #img.show()

    # win环境
    # tesseract 路径
    pytesseract.pytesseract.tesseract_cmd = 'D:\\sina\\software\\Tesseract\\tesseract'
    # 语言包目录和参数
    tessdata_dir_config = '--tessdata-dir "D:\\sina\\software\\Tesseract\\tessdata" --psm 6'

    # mac 环境 记得自己安装训练文件
    # tesseract 路径
    #pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
    # 语言包目录和参数
    #tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract/3.05.01/share/tessdata/" --psm 6'
    
    # lang 指定中文简体
    question = pytesseract.image_to_string(question_im, lang='chi_sim', config=tessdata_dir_config)
    question = question.replace("\n", "")[2:]
    question = question.replace(".", "")
    question = question.replace(" ", "")
    question = question.replace("_", "一")
    question = question.replace("硼", "哪")
    question = question.replace("?", "")

    choice = pytesseract.image_to_string(choices_im, lang='chi_sim', config=tessdata_dir_config)
    choices = choice.strip().split("\n")
    choices = [ x for x in choices if x != '' ]

    return question, choices


if __name__ == '__main__':
    image = Image.open("../screenshot.png")
    question,choices = ocr_img(image)

    print("识别结果:")
    print(question)
    print(choices)