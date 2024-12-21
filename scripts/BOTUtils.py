import os
import smtplib
import subprocess
import PropertiesReader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


##### Send Email
def sendEmail(mail_subject,mail_body):
    msg = MIMEMultipart()
    msg["Subject"] = mail_subject
    msg["From"] = PropertiesReader.getFrom()
    msg["To"] = PropertiesReader.getTo()
    msg["Cc"] = PropertiesReader.getCC()
    body = MIMEText(mail_body)
    msg.attach(body)

    smptserver = PropertiesReader.getSMTPServer()
    smtpport = PropertiesReader.getSMTPPort()


    smtpObj = smtplib.SMTP(smptserver, smtpport)
    smtpObj.starttls()
    smtpObj.login(msg["From"], PropertiesReader.getSMTPPassword())
    smtpObj.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())

    print "Successfully sent email"
    smtpObj.quit()


##### Get Folder Size

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size


#### Check if folder size has breached the threshold 
def getStorageThresholdBreach():
    storage_threshold = PropertiesReader.getStorageThreshold()
    print storage_threshold
    total_used_size = getFolderSize(PropertiesReader.getStorageDir())/1024 /1024 /1024
    print total_used_size
    if (float(total_used_size)/float(storage_threshold))*100 > 90:
        sendEmail(PropertiesReader.getStorageSubject(),PropertiesReader.getStorageBody())
    else:
        print 'Storage within limit'

##### Check Server Status
def checkServerStatus():
    is_up = ''
    with open(os.devnull, 'w') as DEVNULL:
        try:
            subprocess.check_call(
                ['ping', PropertiesReader.getConnectivityServer()],
                stdout=DEVNULL,  # suppress output
                stderr=DEVNULL
            )
            is_up = True
            print 'connectivity is up and running'
        except subprocess.CalledProcessError:
            is_up = False
            sendEmail(PropertiesReader.getConnectivitySubject(),PropertiesReader.getConnectivityBody())


getStorageThresholdBreach()
checkServerStatus()
