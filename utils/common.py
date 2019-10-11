#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib
import json
import time

SPIDER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '
                  'WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
}


def is_json(resp):
    """
    判断数据是否能被 Json 化。 True 能，False 否。
    :param resp: request.
    :return: bool, True 数据可 Json 化；False 不能 JOSN 化。
    """
    try:
        json.loads(resp.text)
        return True
    except AttributeError:
        return False


def md5_encode(text):
    """ 把數據 md5 化 """
    if not isinstance(text, str):
        text = str(text)
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    result = md5.hexdigest().upper()
    return result


def generate_time(format_="%Y-%m-%d"):
    """获取当前日期"""

    local_time = time.localtime(time.time())
    data_head = time.strftime(format_, local_time)
    return data_head
