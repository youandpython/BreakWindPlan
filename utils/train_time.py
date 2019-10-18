#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from xml.etree import ElementTree


def get(train_code):
    url = f'http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode={train_code}&UserID='
    resp = requests.get(url)
    if resp.status_code == 200:
        root = ElementTree.XML(resp.text)
        time_list = list()
        for node in root.iter('TrainDetailInfo'):
            train_station = node.find('TrainStation').text.replace('）', ')').split('（车次：')[0]
            arrive_time = format_time(node.find('ArriveTime').text)
            start_time = format_time(node.find('StartTime').text)
            if not arrive_time:
                time_list.append(f'{train_station},[起点发车]{start_time}')
            elif not start_time:
                time_list.append(f'{train_station},[终点停车]{arrive_time}')
            else:
                time_list.append(f'{train_station},[到]{arrive_time}--{start_time}[离]')
        return '\r\n'.join(time_list)
    return f'未查询到{train_code}运行时刻表'


def format_time(time_str: str):
    if time_str:
        time_list = time_str.strip().split(':')
        return ':'.join(time_list[0:2])


if __name__ == '__main__':
    a = get('k8361')  # K282, K8361
    print(a)
