# -*- coding: utf-8 -*-
import sae
import time
from bottle import *
from config import CFG

#from wechat_sdk.basic import WechatBasic
#from xml import etree
#from xml.etree import ElementTree
import xml.etree.ElementTree as ET

#debug(True)
APP = Bottle()


@APP.get('/')
def web_access():
     return "bookgiver:share books with others"



@APP.get('/echo/')
def checkSignature():
    print request.query.keys()
    print request.query.echostr
    return request.query.echostr



@APP.post('/echo/')
#def wechat_test():
#     #print request.forms.keys()[0]
#     xml = ET.fromstring(request.forms.keys()[0])
#     print xml.findtext("Content")

def wechat_post():
     xml = ET.fromstring(request.forms.keys()[0])
     fromUser = xml.findtext("ToUserName")
     toUser = xml.findtext("FromUserName")
     __MsgType = xml.findtext("MsgType")
     __Content = xml.findtext("Content")
     if "text" == __MsgType:
        if "hi" == __Content:
            tStamp = time.time()
            content = "欢迎！"
            print CFG.TPL_TEXT% locals()
            return CFG.TPL_TEXT% locals()
     return None

