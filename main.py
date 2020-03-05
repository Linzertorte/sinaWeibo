# -*- coding: utf-8 -*-

import send_task
from weibo.weibo_sender import WeiboSender
from weibo.weibo_login import wblogin
from weibo.weibo_message import WeiboMessage

if __name__ == '__main__':
    (wei_session, uid) = wblogin()
    if uid is not None:
        wei_session.get('http://weibo.com/')
        print uid
        sender = WeiboSender(wei_session, uid)
        weibo = WeiboMessage("test",["https://github.com/Linzertorte/linzertorte.github.io/blob/master/3.png?raw=true"])
        sender.send_weibo(weibo)
