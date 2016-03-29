# coding=utf-8

__author__ = 'hohoTT'

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Calibri.ttf', size=90)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-90, 10), '6', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

if __name__ == '__main__':
    image = Image.open('img/hoho.jpg')
    add_num(image)
