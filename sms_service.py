#Interface definition:
#import sms_service
#sms = sms_service(content, phone)
#sms.send

import os
import sys
import urllib
import configparser
import time
import urllib.parse
import urllib.request

class sms_service:

    def __init__(self, content, phone):
        self.api = "http://www.smsgate.cn/gb.asp?"

        self.request = { 'usr' : 'rpci',
            'pwd' : 'rpscm',
            'tel' : phone,
            'msg' : content
           }

        self.query=self.api + urllib.parse.urlencode(self.request)

        self.proxy = urllib.request.ProxyHandler({'http': 'http://fiesprx003.nsn-net.net:8080'})  

        #self.query=query_gen()
        
    def send(self):
        
        opener = urllib.request.build_opener(self.proxy)
        urllib.request.install_opener(opener)
        urllib.request.urlopen(self.query)
        
        print ("sms sent successfully")

