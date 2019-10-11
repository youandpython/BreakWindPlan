#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests


def get():
    """
    彩虹屁生成器
    :return: str,彩虹屁
    """
    try:
        resp = requests.get('https://chp.shadiao.app/api.php')
        if resp.status_code == 200:
            return resp.text
        return '彩虹屁获取失败'
    except Exception:
        return '彩虹屁获取失败'


if __name__ == '__main__':
    a = get()
    print(a)
