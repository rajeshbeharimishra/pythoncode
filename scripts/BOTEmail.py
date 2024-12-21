import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

headers = """From: From Person <rbmishra@infogix.com>
To: To Person <rbmishra@infogix.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

Dear Rajesh, \n Please send your report\n Thank you for your attention
"""

smptserver='smtp.office365.com'
smtpport = 587
sender = 'rbmishra@infogix.com'
recipient = 'rbmishra@infogix.com'



print headers

smtpObj = smtplib.SMTP(smptserver, smtpport)
smtpObj.starttls()
smtpObj.login(sender, '345@Password')
smtpObj.sendmail(sender,recipient,headers)         

print "Successfully sent email"

