#!/usr/bin/python
import os
import subprocess

response=''

##with open(os.devnull, 'w') as DEVNULL:
##    try:
##        subprocess.check_call(
##            ['ping', 'localhost'],
##            stdout=DEVNULL,  # suppress output
##            stderr=DEVNULL
##        )
##        is_up = True
##        print is_up
##    except subprocess.CalledProcessError:
##        is_up = False
##        print is_up


try:
    response = subprocess.check_output(
        ['ping', 'localhost'],
        stderr=subprocess.STDOUT,  # get all output
        universal_newlines=True  # return string not bytes
    )
except subprocess.CalledProcessError:
    response = None

print response

try:
    response3=''
    strPath='C:\\Users\\rbmishra\\Desktop\\sample_data\\sample_data.csv'
    with open('C:\\Users\\rbmishra\\Desktop\\sample_data\\sample_data.csv', 'rb') as mycsvfile:
        try:
            cmd = 'find "20061981" '+ strPath
            print cmd
            response3 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #response3 = subprocess.check_output(cmd, stderr=subprocess.STDOUT,universal_newlines=True)
            print 'here1'
            print response3.communicate()[0].split()
        except subprocess.CalledProcessError:
            print 'here2'
            print response3.stderr
except IOError:
    print "Error: File does not appear to exist."



#response2 = os.system("ping "+ "localhost")
#print response2
