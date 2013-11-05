import os
import sys
import httplib
import urllib2
import ConfigParser
import time
#Purpose: This scripts is used to send out SMS notification
#Parameter Introduction
#usr: user name
#pwd: password
#tel: phone numbers used to receive SMS notification
#msg: message content
#job_name: from upstream failed job

#Setup config parser
config = ConfigParser.RawConfigParser()
config.read('phone_number.txt')

#Get job name from upstream job
job_name = sys.argv[1]
print job_name

#Define contact list and phone number
bm_contact = config.get('Chengdu', 'yuhui') + config.get('Chengdu', 'chenjie')
webpage_contact = config.get('Chengdu', 'mingkailing') + config.get('Chengdu', 'chenjinrui')
rpbuild_contact = config.get('Chengdu', 'yuhui') + config.get('Chengdu', 'maorunsheng')
rsync_contact = config.get('Chengdu', 'zhuke') + config.get('Chengdu', 'maorunsheng')
test_contact = config.get('Chengdu', 'xuhuanchun') + config.get('Chengdu', 'zhaoxiaomin') + config.get('Chengdu', 'guoweiwei')

basic_info = "http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel="

#Generate http query based on job name
def query_gen():
  if "BM-PS" in job_name or "BMPS" in job_name:
     query=basic_info + bm_contact + "&msg=" + job_name + "_failed"
  elif "Webpage" in job_name:
     query=basic_info + webpage_contact + "&msg=" + job_name + "_failed"
  elif "build" in job_name:
     query=basic_info + rpbuild_contact + "&msg=" + job_name + "_failed"
  elif "Rsync" in job_name:
     query=basic_info + rsync_contact + "&msg=" + job_name + "_failed"
  elif "Smoke" in job_name:
     if time.localtime()[3] > 13:
         query=basic_info + test_contact + "&msg=" + job_name + "_failed"
     else:
         print "Chengdu working time, no SMS will be sent"
         sys.exit(0)
  else:
     query=basic_info + rpbuild_contact + "&msg=" + job_name + "_failed"

  return query

query=query_gen()
print query
#Proxy is needed in this env.
proxy = urllib2.ProxyHandler({'http': 'http://fiesprx003.nsn-net.net:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
urllib2.urlopen(query)
