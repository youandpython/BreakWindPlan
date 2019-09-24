#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

# import pytesseract
# from PIL import Image

import config as conf

#
# # 移除背景色
# def remove_background(pic_name):
#     img = get_pic(pic_name)
#     width = img.size[0]  # 长度
#     height = img.size[1]  # 宽度
#     for i in range(0, width):  # 遍历所有长度的点
#         for j in range(0, height):  # 遍历所有宽度的点
#             data = (img.getpixel((i, j)))  # 打印该图片的所有点
#             if data[0] >= 150 and data[1] >= 160 and data[2] >= 0:  # RGBA的r值大于170，并且g值大于170,并且b值大于170
#                 img.putpixel((i, j), (255, 255, 255, 255))  # 则这些像素点的颜色改成大红色
#             else:
#                 img.putpixel((i, j), (0, 0, 0, 0))
#     img = img.convert("RGB")  # 把图片强制转成RGB
#     save_pic(img, pic_name, '去底色')
#     return img
#
#
# # 二值化变色
# def binaryzation(pic_name):
#     img = get_pic(pic_name)
#     w, h = img.size
#     for x in range(w):
#         for y in range(h):
#             r, g, b = img.getpixel((x, y))
#             if 190 <= r <= 255 and 170 <= g <= 255 and 0 <= b <= 140:
#                 img.putpixel((x, y), (0, 0, 0))
#             if 0 <= r <= 90 and 210 <= g <= 255 and 0 <= b <= 90:
#                 img.putpixel((x, y), (0, 0, 0))
#     img = img.convert('L').point([0] * 150 + [1] * (256 - 150), '1')
#     save_pic(img, pic_name, '二值化')
#     return img
#
#
# def smartSliceImg(pic_name, outDir, count=4, p_w=3):
#     '''
#     :param img:
#     :param outDir:
#     :param count: 图片中有多少个图片
#     :param p_w: 对切割地方多少像素内进行判断
#     :return:
#     '''
#     img = get_pic(pic_name)
#     w, h = img.size
#     pixdata = img.load()
#     eachWidth = int(w / count)
#     beforeX = 0
#     for i in range(count):
#
#         allBCount = []
#         nextXOri = (i + 1) * eachWidth
#
#         for x in range(nextXOri - p_w, nextXOri + p_w):
#             if x >= w:
#                 x = w - 1
#             if x < 0:
#                 x = 0
#             b_count = 0
#             for y in range(h):
#                 if pixdata[x, y] == 0:
#                     b_count += 1
#             allBCount.append({'x_pos': x, 'count': b_count})
#         sort = sorted(allBCount, key=lambda e: e.get('count'))
#
#         nextX = sort[0]['x_pos']
#         box = (beforeX, 0, nextX, h)
#         img.crop(box).save(os.path.join(outDir, pic_name + str(i) + ".png"))
#         beforeX = nextX
#
#
# def get_all_pic():
#     return [files for root, dirs, files in os.walk(os.path.join(conf.pic_temp_path, 'test'))][0]
#
#
# def save_pic(pic_os, pic_name, tag):
#     pic_os.save(os.path.join(conf.pic_temp_path, tag, pic_name))
#
#
# def get_pic(pic_name):
#     im = Image.open(os.path.join(conf.pic_temp_path, 'test', pic_name))
#     return im
#
#
# def print_digit(img):
#     digit = pytesseract.image_to_string(img, config='digits').strip()
#     print(digit)
#
#
# # rownum：切割行数；colnum：切割列数；dstpath：图片文件路径；img_name：要切割的图片文件
# def splitimage(rownum=1, colnum=4, dstpath='', img_name=''):
#     img = Image.open(img_name)
#     w, h = img.size
#     if rownum <= h and colnum <= w:
#         print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
#         print('开始处理图片切割, 请稍候...')
#
#         s = os.path.split(img_name)
#         if dstpath == '':
#             dstpath = s[0]
#         fn = s[1].split('.')
#         basename = fn[0]
#         ext = fn[-1]
#
#         num = 1
#         rowheight = h // rownum
#         colwidth = w // colnum
#         file_list = []
#         for r in range(rownum):
#             index = 0
#             for c in range(colnum):
#                 if index < 1:
#                     colwid = colwidth + 6
#                 elif index < 2:
#                     colwid = colwidth + 1
#                 elif index < 3:
#                     colwid = colwidth
#
#                 box = (c * colwid, r * rowheight, (c + 1) * colwid, (r + 1) * rowheight)
#                 newfile = os.path.join(dstpath, basename + '_' + str(num) + '.' + ext)
#                 file_list.append(newfile)
#                 img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
#                 num = num + 1
#                 index += 1
#         for f in file_list:
#             print(f)
#         print('图片切割完毕，共生成 %s 张小图片。' % num)
#
#
# if __name__ == '__main__':
#     pics = get_all_pic()
#     for index, pic_path in enumerate(pics):
#         # print_digit(remove_background(pic_path))
#         # print_digit(binaryzation(pic_path))
#         smartSliceImg(pic_path, os.path.join(conf.pic_temp_path, '切图1'), count=16)
#         print(index)
