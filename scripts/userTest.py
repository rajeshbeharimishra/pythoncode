#!/usr/bin/env python
import sys

class User:
    name = ""
    age = 0
    height = 0
    weight = 0
    
    def display(self):
        print ''
        print 'User Information:'
        print 'User Name  :', self.name
        print 'User Age   :', self.age
        print 'User Height:', self.height
        print 'User Weight:', self.weight
    
    def loadFromInput(self):
        self.name = raw_input('Enter User Name: ')
        self.age = int(raw_input('Enter Age: '))
        self.height = float(raw_input('Enter Height (in feet): '))
        self.weight = int(raw_input('Enter Weight: '))
    
    def save(self):
        f = open('user.info','w')
        f.write(self.name + '\n')
        f.write(str(self.age) + '\n')
        f.write(str(self.height) + '\n')
        f.write(str(self.weight) + '\n')
        f.close()
        
    def loadFromFile(self):
    	f = open('user.info', 'r')
    	self.name = f.readline().rstrip()
    	self.age = int(f.readline())
    	self.height = float(f.readline())
    	self.weight = int(f.readline())

        
theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
    theUser = User()
    theUser.loadFromFile()
else:
    theUser = User()
    theUser.loadFromInput()
    theUser.save()
    
theUser.display()