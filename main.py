import sms_service

content = "first try"

phone = "18080115634"

sms_client = sms_service.sms_service(content,phone)

result = sms_client.send()
