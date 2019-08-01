#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from wxpy import *

import config as config
import load as load
import wx_reply as wx_reply


# 微信机器人，缓存登录信息，调用初始化方法
bot = Bot(cache_path=True, qr_path=config.qr_path)
# 加载配置信息到机器人
load.load_config_to_bot(bot)

"""群功能"""


@bot.register(chats=Group)
def group_msg(msg):
    """接收群消息"""
    if msg.type == TEXT:
        # 群回复
        if msg.bot.is_group_reply:
            # 不用@直接回复
            wx_reply.auto_reply(msg)
    else:
        pass
    return None


# 互交模式，阻塞线程，使程序一直运行
embed()
