import sms_service.py

content = "first try"

phone = "18080115634"

sms_client = sms_service.py(content,phone)

result = sms_client.send()

print (result)