# -*- coding:utf-8 -*-s
import sae
import config
from bottle import *
from web import APP
#import os
#import sys

#root = os.path.dirname(__file__)
#sys.path.insert(0, os.path.join(root, 'site-packages'))

#导入Bottle模块
#from bottle import *
#from wechat_sdk.basic import WechatBasic
#from xml import etree
#from xml.etree import ElementTree

#app=Bottle()

#debug(True)  #打开debug功能

#@app.get('/')
#def checkSignature():
     # 你在微信公众平台上设置的TOKEN
#     token = "bookgiverpy"
#     wechat = WechatBasic(token=token)
#     signature = request.GET.get('signature', None)  
#     timestamp = request.GET.get('timestamp', None)
#     nonce = request.GET.get('nonce', None)
#     if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
#      return request.GET.get('echostr', None);
#     return "bookgiver:share books with others"


application = sae.create_wsgi_app(APP)
