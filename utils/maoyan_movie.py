#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import time
from utils.common import SPIDER_HEADERS, generate_time, is_json


def get():
    """
     获取特定日期的实时票房日期
     https://piaofang.maoyan.com/second-box?beginDate=20190830#指定日期的节假日及万年历信息
    :rtype str
    """
    date_ = generate_time('%Y%m%d')
    try:
        url = 'https://piaofang.maoyan.com/second-box?beginDate={}'.format(date_)
        resp = requests.get(url, headers=SPIDER_HEADERS)

        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            if content_dict['success']:
                cur_date = time.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
                data_dict = content_dict['data']
                total_box_info = data_dict['totalBoxInfo']
                box_list = data_dict['list']
                box_info_list = []

                for i, r in enumerate(box_list[:10]):
                    movie_name = r['movieName']
                    box_info = r['boxInfo']
                    sum_box_info = r['sumBoxInfo']
                    release_info = r['releaseInfo']
                    box_info_list.append(f'{str(i + 1)}.《{movie_name}》({box_info}万,{release_info},累积:{sum_box_info})')

                box_info = '\r\n'.join(box_info_list)
                return_text = f"{cur_date} 票房信息\r\n当日总票房：{total_box_info}万\r\n{box_info}"
                return return_text
            else:
                return '获取票房失败:{}'.format(content_dict['msg'])
    except Exception:
        return '获取票房失败。'


if __name__ == '__main__':
    dd = get()
    print(dd)
