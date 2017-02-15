# -*- coding: utf-8 -*-
#最后修改时间：20160702,19:00
import os
import sys
import re

root = os.path.dirname(__file__)
reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.insert(0, os.path.join(root, 'site-packages'))
########SAE模块################
import sae.kvdb
import werobot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.reply import ArticlesReply, Article,TextReply
########外部模块################
from modules import tuling123

session_storage = SaeKVDBStorage()
robot = werobot.WeRoBot(token="qwert12345", enable_session=True,session_storage=session_storage)

########配置################
multiuser = False
########主程序################
@robot.filter("瓶子注册")
def pingzi(message, session):
    session["pingzi"] = message.source
    return '哈哈，我记住你了'

@robot.filter("zhnja")
def zhnja(message, session):
    session["zhnja"] = message.source
    reply = TextReply(message = message,content = "hellozhnja.")
    return reply
    #return '哈哈，我记住你了'

@robot.filter("openid")
def openid(message, session):
    session[message.source] = message.source 
    if session.get(message.source,0) == message.source :
        return 'you are already in system ' + str(message.source)
    else:
        return 'your openid is ' + str(message.source)

# @robot.filter("投票")
# def vote(message,session):
#     session[message.source] = message.source 
#     reply = ArticlesReply(message=message)
#     article = Article(
#         title = "投票页面",
#         description = "第一个微信投票",
#         url = "http://mp.weixin.qq.com/s?__biz=MjM5NzYyNDE0Mg==&mid=2247483652&idx=1&sn=433a18a7ae7a0a652cc670603ed2a6dc&scene=0#wechat_redirect"
#     )
#     reply.add_article(article)
#     return article
@robot.filter("投票")
def vote(message):
    return [
        [
            "title",
            "description",
            "img",
            "url"
        ],
        [
            "投票页面",
            "第一个微信投票",
            "",
            "http://mp.weixin.qq.com/s?__biz=MjM5NzYyNDE0Mg==&mid=2247483652&idx=1&sn=433a18a7ae7a0a652cc670603ed2a6dc&scene=0#wechat_redirect"
        ]
    ]

@robot.text
def users(message, session):
    if multiuser:
        if message.source == session["zhnja"]:
            return talktozhnja(message.content)
        elif message.source == session["pingzi"]:
            return talktopingzi(message.content)
        else:
            return "who are you?"
    else:
        return talktoall(message.content)

@robot.handler
def echo(message):
    return 'Hello World!'


########中间函数################
def talktopingzi(message):
    return "hello,pingzi"

def talktozhnja(message):
    return "hello,zhnja"

def talktoall(message):
    message = message.replace(' ','')
    return tuling123(message)