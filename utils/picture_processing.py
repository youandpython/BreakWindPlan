#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PIL import Image


def create_nike_image(pic_path, water_mark_path, pic_with_watermark_path):
    # 打开头像
    nike_image = Image.open(pic_path)
    # 创建底图
    target = Image.new('RGB', (nike_image.width, nike_image.height), (0, 0, 0, 0))
    # 打开装饰
    logo = Image.open(water_mark_path)
    # 缩放logo图片
    logo.thumbnail((nike_image.width * 0.5, nike_image.height * 0.5))
    # 分离透明通道
    r, g, b, a = logo.split()
    # 将头像贴到底图
    position = (0, (nike_image.height - logo.height))
    nike_image.convert("RGBA")
    target.paste(nike_image, (0, 0))
    # 将装饰贴到底图
    logo.convert("RGBA")
    target.paste(logo, position, mask=a)
    # 保存图片
    target.save(pic_with_watermark_path)


if __name__ == '__main__':
    create_nike_image(r'E:\Python3_Test\BreakWindPlan\pic_temp\head_pic\tx.jpg',
                      r'E:\Python3_Test\BreakWindPlan\pic_temp\head_water_mark\hzw.png',
                      r'E:\Python3_Test\BreakWindPlan\pic_temp\tx1.jpg')
