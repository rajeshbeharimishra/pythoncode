#!/usr/bin/python    
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('BOTConfigFile.properties')

# Getting DB Connection Strings

def getCARAConnectionURL():
    return config.get('DatabaseSection', 'database.cara.con') 

def getFMSConnectionURL():
    return config.get('DatabaseSection', 'database.fms.con')

# Getting External Website URLs

def getABNURL():
    return config.get('URLSection', 'abn.url')

def getRentURL():
    return config.get('URLSection', 'rent.url')

def getBuyURL():
    return config.get('URLSection', 'buy.url')


# Getting Base Directories for Individual Modules
def getInputDir():
    return config.get('DirectorySection', 'input.dir')

def getMICADir():
    return config.get('DirectorySection', 'mica.dir')

def getCARADir():
    return config.get('DirectorySection', 'cara.dir')

def getABNDir():
    return config.get('DirectorySection', 'abn.dir')

def getACNDir():
    return config.get('DirectorySection', 'acn.dir')

def getVPBDir():
    return config.get('DirectorySection', 'vpb.dir')

def getVPRDir():
    return config.get('DirectorySection', 'vpr.dir')

def getSummaryDir():
    return config.get('DirectorySection', 'summary.dir')



# Getting Log Directories
def getInputLogDir():
    return config.get('LogSection', 'input.log.dir')

def getMICALogDir():
    return config.get('LogSection', 'mica.log.dir')

def getCARALogDir():
    return config.get('LogSection', 'cara.log.dir')

def getABNLogDir():
    return config.get('LogSection', 'abn.log.dir')

def getACNLogDir():
    return config.get('LogSection', 'acn.log.dir')

def getVPBLogDir():
    return config.get('LogSection', 'vpb.log.dir')

def getVPRLogDir():
    return config.get('LogSection', 'vpr.log.dir')

def getSummaryLogDir():
    return config.get('LogSection', 'summary.log.dir')

def getAttachmentLogDir():
    return config.get('LogSection', 'attachment.log.dir')



# Getting Queries
def getCARAQuery():
    return config.get('QuerySection', 'cara.query')

def getInputQuery():
    return config.get('QuerySection', 'input.query')


# Getting Extensions
def getOutputExtension():
    return config.get('ExtSection', 'output.ext')

def getLogExtension():
    return config.get('ExtSection', 'log.ext')

def getErrorExtension():
    return config.get('ExtSection', 'error.ext')

def getTempExtension():
    return config.get('ExtSection', 'temp.ext')

def getInputExtension():
    return config.get('ExtSection', 'input.ext')


# Getting Keys
def getCaraOutputKey():
    return config.get('KeySection', 'cara.output.key')

def getCaraErrorLogKey():
    return config.get('KeySection', 'cara.error.key')
	
def getInputKey():
    return config.get('KeySection', 'input.key')

def getInputErrorLogKey():
    return config.get('KeySection', 'input.error.key')
	
def getAttachmentKey():
    return config.get('KeySection', 'attachment.error.key')


# Email Section
def getSMTPServer():
    return config.get('EmailSection', 'email.smtp.server')

def getSMTPPort():
    return config.get('EmailSection', 'email.smtp.port')

def getSMTPPassword():
    return config.get('EmailSection', 'email.smtp.password')

def getFrom():
    return config.get('EmailSection', 'email.smtp.from')

def getTo():
    return config.get('EmailSection', 'email.smtp.to')

def getCC():
    return config.get('EmailSection', 'email.smtp.cc')


#Storage Section

def getStorageDir():
    return config.get('StorageSection', 'storage.dir')

def getStorageThreshold():
    return config.get('StorageSection', 'storage.threshold')

def getStorageSubject():
    return config.get('StorageSection', 'storage.subject')

def getStorageBody():
    return config.get('StorageSection', 'storage.body')


#Connectivity Section
def getConnectivitySubject():
    return config.get('ConnectivitySection', 'connection.status.subject')

def getConnectivityBody():
    return config.get('ConnectivitySection', 'connection.status.body')

def getConnectivityServer():
    return config.get('ConnectivitySection', 'connectivity.status.server')
