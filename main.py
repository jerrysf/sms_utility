import sms_service

content = "first_try"

phone = "18228029575"

sms_client = sms_service.sms_service(content,phone)

result = sms_client.send()
