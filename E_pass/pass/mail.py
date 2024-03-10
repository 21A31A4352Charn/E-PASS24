import smtplib
from string import Template
from pathlib import Path
def mails(mail_reciver,msg):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('surendra.sathireddy100@gmail.com','quanmnwjlczqlwaz')
    msg=msg
    s.sendmail('surendra.sathireddy100@gmail.com',mail_reciver, msg)
    s.quit()
    print("sussesfull sent")


'''#password:-quanmnwjlczqlwaz

sms='AC14cb5767ad61de7bea4c24755b9f88f7'

Auth_token= '1c1d911013a057a29d2f3b7372e9bae4'


Twililo_phone_number= +15075541510




from twilio.rest import Client

client=Client('AC14cb5767ad61de7bea4c24755b9f88f7','1c1d911013a057a29d2f3b7372e9bae4')

message=client.messages.create(
    body="This message is from student",
    from_='+15075541510',
    to='+918125977682')

print(message.body)




#---->9kpNWKxfebAQRgyoh87VL2csja0En4zwdHq3YFrGC6XSBZtMTvJqm7KeFRazhldW30ncOjgkwI48X1pG'''