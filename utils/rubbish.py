#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from utils.common import SPIDER_HEADERS, is_json


def get(key):
    """
    # http://www.atoolbox.net/Tool.php?Id=804
    :param key:
    :return:
    """
    params = {'key': key}
    resp = requests.get('http://www.atoolbox.net/api/GetRefuseClassification.php',
                        headers=SPIDER_HEADERS,
                        params=params)
    try:
        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            if not content_dict:
                raise Exception()

            return_list = list(content_dict.values())
            type_list = [rl['type'] for rl in return_list if key == rl['name']]
            if len(type_list):
                return ','.join(list(set(type_list)))
            else:
                other = '\r\n'.join(f"{i['name']}:{i['type']}" for i in return_list[:6])
                return other
        return f'未查询到{key}的所属分类'
    except Exception:
        return f'未查询到{key}的所属分类'


if __name__ == '__main__':
    a = get('奶茶')
    print(a)
