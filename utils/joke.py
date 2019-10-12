#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from utils.common import is_json, SPIDER_HEADERS
import re
import random

rule_joke = re.compile('<span id=\"text110\">([\w\W]*?)</span>')
rule_url = re.compile('<a href=\"(.*?)\"target=\"_blank\" >')
mainUrl = 'http://www.jokeji.cn'
url = 'http://www.jokeji.cn/list.htm'


def get():
    try:
        resp = requests.get(url, headers=SPIDER_HEADERS)
        if resp.status_code == 200:
            urls = rule_url.findall(resp.content.decode('GBK'))
            if len(urls) <= 0:
                return '笑话暂时没想好，等我想想~'
            index = random.sample(range(len(urls)), 1)[0]

            joke_url = mainUrl + urls[index]
            resp2 = requests.get(joke_url, headers=SPIDER_HEADERS)
            if resp2.status_code == 200:
                joke_str = rule_joke.findall(resp2.content.decode('GBK'))
                jokes = joke_str[0].split('<P>')[1:]
                if len(jokes) <= 0:
                    return '笑话暂时没想好，等我想想~'
                index2 = random.sample(range(len(jokes)), 1)[0]
                result = jokes[index2].replace('</P>', '').replace('<BR>', '').split('、')
                return result[1]
    except Exception:
        return '笑话暂时没想好，等我想想~'


def get_1():
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
