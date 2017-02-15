# -*- coding: utf8 -*-
  
import json
import urllib2


def tuling123(message):
    url = 'http://www.tuling123.com/openapi/api?key=' + "61f0b2c55b87e7622a83821bce86b2d2" + '&info=' + message
    re = urllib2.urlopen(url).read()
    re_dict = json.loads(re)
    text = re_dict['text']
    return text