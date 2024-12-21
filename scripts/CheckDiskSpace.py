import os
import PropertiesReader

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

def getStorageThresholdBreach():
    storage_threshold = PropertiesReader.getStorageThreshold()
    print storage_threshold
    total_used_size = getFolderSize(PropertiesReader.getStorageDir())/1024 /1024 /1024
    print total_used_size
    if (float(total_used_size)/float(storage_threshold))*100 > 90:
        return True
    else:
        return False

print "Size in GB: " + str((getFolderSize(PropertiesReader.getStorageDir())/1024 /1024 /1024))

print getStorageThresholdBreach()
