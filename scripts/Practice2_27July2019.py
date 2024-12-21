i=0
while(i<10):
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
    i=i+1

j=0
for j in range(11,20):
    if(j%2==0):
        print(j,"is even")
    else:
        print(j,"is odd")
    j=j+1


s="Hello"
while (s=="Hello"):
    secret_word = input("You're stuck in an infinite loop! Enter a secret word to leave the loop:")
    if(secret_word=="chupacabra"):
        break
print("finally you are out of infinite loop")

a=0
b= not not a
print(b)

x=4
y=8
print("Bitwise & Result", x&y)
print("Bitwise | Result", x|y)
print("Bitwise ^ Result", x^y)
print("Bitwise ~ Result", ~x)

var=17
varRight = var >>1
varLeft = var<<2
print(var, varRight, varLeft)

myList = [2,9.8,7,6,5,3,1,11]
sum=0
for i in range(len(myList)):
    sum = sum+myList[i]
print(sum)

newSum =0
for j in myList:
    newSum = newSum+j
print(newSum)

myList.sort()
print(myList)
