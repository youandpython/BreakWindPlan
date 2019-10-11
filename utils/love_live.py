#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests


def get():
    """
    从土味情话中获取每日一句。
    :return: str,土味情话。
    """
    try:
        resp = requests.get('https://api.lovelive.tools/api/SweetNothings')
        if resp.status_code == 200:
            return resp.text
    except Exception:
        return None


if __name__ == '__main__':
    a = get()
    print(a)
