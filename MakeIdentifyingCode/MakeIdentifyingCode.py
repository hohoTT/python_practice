# coding=utf-8

__author__ = 'hohoTT'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random
import os

# 使用的Windows中自带的字体样式
fontPath = "C:/windows/fonts/Calibri.ttf"


# 获得随机四个字母
def getRandomChar():
    return [random.choice(string.letters) for _ in range(4)]


# 获得颜色
def getRandomColor():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))


# 获得验证码图片
def getCodePiture():
    width = 240
    height = 60
    # 创建画布
    image = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype(fontPath, 40)
    draw = ImageDraw.Draw(image)
    # 创建验证码对象
    code = getRandomChar()
    # 把验证码放到画布上
    for t in range(4):
        draw.text((60 * t + 10, 0), code[t], font=font, fill=getRandomColor())
    # 填充噪点
    for _ in range(random.randint(1500, 3000)):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=getRandomColor())
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    # 保存名字为验证码的图片
    # 这里使用的是os.path.join(路径，图像文件名)，使得图片文件保存到resultImg文件夹中
    imgPath = os.path.join("resultImg", "".join(code) + '.jpg')
    image.save(imgPath, 'jpeg')

if __name__ == '__main__':
    getCodePiture()
