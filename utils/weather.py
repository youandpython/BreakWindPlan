#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import re

import requests


def get(city_name):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city_name
    response = requests.get(url)
    weather_json = json.loads(response.text)
    info = list()
    if "data" not in weather_json:
        info.append('未查询到{}'.format(city_name))
    else:
        a = weather_json['data']
        info.append('{0} 当前温度：{1}℃'.format(a['city'], a['wendu']))
        info.append('温馨提示：{}'.format(a['ganmao']))
        info.append("-----------------------------")
        for i in range(1, 3):
            info.append('{0} {1}'.format(a["forecast"][i]['date'], a["forecast"][i]['type']))
            feng_li = a["forecast"][i]['fengli'][9: [m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]]
            info.append('{0} {1}'.format(a["forecast"][i]['fengxiang'], feng_li))
            info.append(a["forecast"][i]['high'])
            info.append(a["forecast"][i]['low'])
            info.append("-----------------------------")
    return '\r\n'.join(info)


if __name__ == '__main__':
    get('南京')
