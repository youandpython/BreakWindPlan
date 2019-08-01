#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 好友功能
import utils.weather as weather
import utils.metro_timetable as metro
import utils.lunar as lunar
import utils.music_platform as music


def auto_reply(msg):
    """自动回复"""
    # 关键字回复
    keyword_reply(msg)


def keyword_reply(msg):
    """关键字回复"""
    text = msg.text.lower()
    if text.startswith('tq'):
        info = tq_info(text, 'tq')
        return msg.reply(info)
    elif text.startswith('dt'):
        info = dt_info(text, 'dt')
        return msg.reply(info)
    elif text == 'hl':
        info = lunar.get()
        return msg.reply(info)
    elif text.startswith('mc'):
        info = mc_info(text, 'mc')
        return msg.reply(info)
    pass


def tq_info(text, tag):
    dm = text.lstrip(tag).strip()
    if len(dm) > 0:
        info = weather.get(dm)
        return info
    return '输入格式不正确'


def dt_info(text, tag):
    dm = text.lstrip(tag).strip()
    if len(dm) > 0:
        dms = dm.split(' ')
        if len(dms) == 2:
            info = metro.get(dms[0], dms[1])
            return info
        if len(dms) == 1:
            info = metro.get(dms[0], '')
            return info
    return '输入格式不正确'


def mc_info(text, tag):
    dm = text.lstrip(tag).strip()
    if len(dm) > 0:
        info = music.get(dm)
        return info
    return '输入格式不正确'
