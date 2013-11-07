import os
import sys
import urllib
import configparser
import time
import urllib.parse
import urllib.request

class sms_service:
      ''' class used for send sms message'''

    def init(self, content, phone):
        ''' generate http request based on input parameters'''
        
        api = "http://www.smsgate.cn/gb.asp?"
        
        request = { 'usr' : 'rpci',
            'pwd' : 'rpscm',
            'tel' : phone,
            'msg' : content
           }
           
        query=api + urllib.parse.urlencode(request) 

        proxy = urllib.request.ProxyHandler({'http': 'http://fiesprx003.nsn-net.net:8080'})  

        query=query_gen()        
    
    def send(self):
        ''' send this message '''
    
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        urllib.request.urlopen(query)

