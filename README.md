# python_practice

python练习册，用于日常python的练习，都是比较有意思的程序


-----------------------------------------------------------------------------------------------------------------------------------------


一、项目ImgTransformCharImg为python将图片转化成字符画的程序

  实现图片转化为字符图画，具体图片具体分析，一张图片从图像到字符不是一蹴而就的，需要经过很多步骤，成品是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
  
  我们是要转换一张彩色的图片，这么这么多的颜色，要怎么对应到字符上去？这里就要介绍灰度值的概念了。
  
      灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
   
  灰度值大的用列表开头的符号，灰度值小的用列表末尾的符号。   
  
