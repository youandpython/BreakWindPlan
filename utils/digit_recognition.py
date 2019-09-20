#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytesseract
from PIL import Image

if __name__ == '__main__':
    test = pytesseract.image_to_string(Image.open(r'C:\Users\11543\Desktop\123.png'), lang='eng')
    print(test)
