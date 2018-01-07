#!/usr/bin/python
# -*- coding: utf8 -*-
  
import os
import json
import urllib2
  
  
class Chat(object):
    key = "61f0b2c55b87e7622a83821bce86b2d2"    
    apiurl = "http://www.tuling123.com/openapi/api?"
  
    def init(self):
        os.system("clear")
        print "尽情调教把!"
        print "-------------------------------"
  
    def get(self):
        print "> ",
        info = raw_input()
        if info == 'q' or info == 'exit' or info == "quit":
            print "- Goodbye"
            return
        self.send(info)
  
    def send(self, info):
        url = self.apiurl + 'key=' + self.key + '&' + 'info=' + info
        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        text = re_dict['text']
        print text
        self.get()
  
  
if __name__ == "__main__":
    print "start"
    chat = Chat()
    chat.init()
    chat.get()
