#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import string

import requests
from utils.common import is_json, SPIDER_HEADERS
import re
import random

rule_joke = re.compile('<span id=\"text110\">([\w\W]*?)</span>')
rule_url = re.compile('<a href=\"(.*?)\"target=\"_blank\" >')
mainUrl = 'http://www.jokeji.cn'
url = 'http://www.jokeji.cn/list.htm'

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
    ]


def get_random_param(count: int):
    return ''.join(random.sample(string.ascii_letters, count))


def get():
    try:
        user_agent = {'User-Agent': random.sample(user_agent_list, 1)[0]}
        resp = requests.get(url, headers=user_agent)
        if resp.status_code == 200:
            urls = rule_url.findall(resp.content.decode('GBK'))
            if len(urls) <= 0:
                return '笑话暂时没想好，等我想想~'
            index = random.sample(range(len(urls)), 1)[0]

            joke_url = mainUrl + urls[index]
            resp2 = requests.get(joke_url, headers=user_agent)
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
