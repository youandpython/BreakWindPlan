#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from utils.common import is_json


def get():
    """
    从词霸中获取每日一句，带英文。
    :return:str ,返回每日一句（双语）
    """
    try:
        resp = requests.get('http://open.iciba.com/dsapi')
        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            content = content_dict.get('content')
            note = content_dict.get('note')
            return '{}\r\n{}'.format(content, note)
    except Exception:
        return None


if __name__ == '__main__':
    a = get()
    print(a)
