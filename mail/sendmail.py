# -*- coding: utf-8 -*- 

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

def account():
    f = open("/home/pi/workspace/raspi-audio/mail/gmail.conf")
    res = f.read()
    ary = res.split("\n")
    f.close()
    ACCOUNT = ary[0]
    PASSWORD = ary[1]
    return ACCOUNT, PASSWORD

if __name__ == "__main__":

    from_address = "tamonbyoe@gmail.com"
    to_address   = "siida0118@gmail.com"

    charset = "ISO-2022-JP"
    subject = u"メールの件名です"
    text    = u"メールの本文です"
    
    msg = MIMEText(text.encode(charset),"plain",charset)
    msg["Subject"] = Header(subject,charset)
    msg["From"]    = from_address
    msg["To"]      = to_address
    msg["Date"]    = formatdate(localtime=True)

    smtp = smtplib.SMTP("smtp.gmail.com",587)				# submission port
    smtp.starttls()											# starttls
    ACC = account()											# read Account
    smtp.login(ACC[0], ACC[1])								# login
    smtp.sendmail(from_address,to_address,msg.as_string())
    smtp.close()
