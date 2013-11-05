#Purpose: This scripts is used to send out SMS notification
#Environment: Python3
#Parameter Introduction
#usr: user name
#pwd: password
#tel: phone numbers used to receive SMS notification
#msg: message content
#job_name: from upstream failed job

import os
import sys
import urllib
import configparser
import time
import urllib.parse
import urllib.request


#Setup config parser
config = configparser.RawConfigParser()
config.read('phone_number.txt')

#Get job name and build number from upstream job
job_name = sys.argv[1]
if len(sys.argv) < 3:
  build_number = ''
else:
  build_number = sys.argv[2]
print (job_name)  
print (build_number)

#Define contact list and phone number
bm_contact = config.get('Chengdu', 'yuhui') + config.get('Chengdu', 'chenjie')
webpage_contact = config.get('Chengdu', 'mingkailing') + config.get('Chengdu', 'chenjinrui')
rpbuild_contact = config.get('Chengdu', 'yuhui') + config.get('Chengdu', 'maorunsheng') + config.get('Chengdu', 'zhuke')
rsync_contact = config.get('Chengdu', 'zhuke') + config.get('Chengdu', 'maorunsheng')
test_contact = config.get('Chengdu', 'xuhuanchun') + config.get('Chengdu', 'zhaoxiaomin') + config.get('Chengdu', 'guoweiwei')
prepare_contact = config.get('Chengdu', 'zhuke')

api = "http://www.smsgate.cn/gb.asp?"

request = { 'usr' : 'rpci',
            'pwd' : 'rpscm',
            'tel' : '18615761805',
            'msg' : job_name + "_failed" + "@" + build_number
           }

#Generate http query based on job name
def query_gen():
  if "BM-PS" in job_name or "BMPS" in job_name:
     request['tel']=bm_contact
  elif "Webpage" in job_name:
     request['tel']=webpage_contact
  elif "build" in job_name:
     request['tel']=rpbuild_contact
  elif "Rsync" in job_name:
     request['tel']=rsync_contact
  elif "prepare" in job_name:
     request['tel']=prepare_contact
  elif "Smoke" in job_name:
     if time.localtime()[3] > 13:
         request['tel']=test_contact
     else:
         print ("Chengdu working time, no SMS will be sent")
         sys.exit(0)
  else:
    #request['tel']=rpbuild_contact
    pass

  query=api + urllib.parse.urlencode(request)   
     
  return query

query=query_gen()

#Proxy is needed in this env.
proxy = urllib.request.ProxyHandler({'http': 'http://fiesprx003.nsn-net.net:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
urllib.request.urlopen(query)
