import os
import sys
import httplib
import urllib2
import time
#Purpose: This scripts is used to send out SMS notification
#Parameter Introduction
#usr: user name
#pwd: password
#tel: phone numbers used to receive SMS notification
#msg: message content
#job_name: from upstream failed job
job_name = sys.argv[1]
print job_name
#Define contact list and phone number
bm_contact = "18615761805;18228029575"
webpage_contact = "13880663304;18116572713" 
rpbuild_contact = "18615761805;15902818862"
rsync_contact = "18615761805;15902818862;18116572713"
testing_contact = "15982007548;18602875770;13881764165"
#Generate http query
if "BM-PS" in job_name: 
   query="http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=" + bm_contact + "&msg=" + job_name + "_failed"
elif "Webpage" in job_name:
   query="http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=" + webpage_contact + "&msg=" + job_name + "_failed"
elif "build" in job_name:
   query="http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=" + rpbuild_contact + "&msg=" + job_name + "_failed"
elif "Rsync" in job_name:
   query="http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=" + rsync_contact + "&msg=" + job_name + "_failed"
elif "Smoke" in job_name:
   if time.localtime()[3] > 13:
       query="http://www.smsgate.cn/gb.asp?usr=rpci&pwd=rpscm&tel=" + testing_contact + "&msg=" + job_name + "_failed"
   else:
       print "Chengdu working time, no SMS will be sent"
       sys.exit(0)
#Proxy is needed in this env.
proxy = urllib2.ProxyHandler({'http': 'http://fiesprx003.nsn-net.net:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
urllib2.urlopen(query)

