#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from utils.common import is_json


def get():
    """
    随机获取笑话段子列表(https://github.com/MZCretin/RollToolsApi#随机获取笑话段子列表)
    :return: str,笑话。
    """
    try:
        resp = requests.get('https://www.mxnzp.com/api/jokes/list/random')
        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            if content_dict['code'] == 1:
                # 每次返回 10 条笑话信息，只取一次
                return_text = content_dict['data'][0]['content']
                return return_text
            else:
                return content_dict['msg']
        return '获取笑话失败。'
    except Exception:
        return '获取笑话失败。'


if __name__ == '__main__':
    a = get()
    print(a)
