#!/usr/bin/python 
import smtplib
import PropertiesReader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["Subject"] = PropertiesReader.getStorageSubject()
msg["From"] = PropertiesReader.getFrom()
msg["To"] = PropertiesReader.getTo()
msg["Cc"] = PropertiesReader.getCC()
body = MIMEText(PropertiesReader.getStorageBody())
msg.attach(body)

smptserver=PropertiesReader.getSMTPServer()
smtpport = PropertiesReader.getSMTPPort()


print msg

smtpObj = smtplib.SMTP(smptserver, smtpport)
smtpObj.starttls()
smtpObj.login(msg["From"], '345@Password')
smtpObj.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())

print "Successfully sent email"
smtpObj.quit()

