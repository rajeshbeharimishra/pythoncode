Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(6/3)
2.0
>>> print(6/3.)
2.0
>>> print(6./3)
2.0
>>> print(6./3.)
2.0
>>> print(6//3)
2
>>> print(6.//3.)
2.0
>>> print(6.//3)
2.0
>>> print(6//4)
1
>>> print(6/4)
1.5
>>> print(6.//4)
1.0
>>> print(6.//-4)
-2.0
>>> print(-6//4)
-2
>>> print(14%4)
2
>>> print(3%2)
1
>>> print(29%3)
2
>>> print(12%4.5)
3.0
>>> print(-4-4)
-8
>>> prit(4.-8)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    prit(4.-8)
NameError: name 'prit' is not defined
>>> print(4.-8)
-4.0
>>> print(-1.1)
-1.1
>>> print(2+3*5)
17
>>> print(2+3*24/3)
26.0
>>> print(9%6%2)
1
>>> print(9//6%2)
1
>>> print(9/6%2)
1.5
>>> print(2**2**3)
256
>>> print(2*3%5)
1
>>> print(5*(25%13)+100)
160
>>> var=1
>>> print(var)
1
>>> account_balance=1000.00
>>> cust_name='Rajesh Mishra'
>>> print(var,account_name,cust_name)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(var,account_name,cust_name)
NameError: name 'account_name' is not defined
>>> print(var, account_balance,cust_name)
1 1000.0 Rajesh Mishra
>>> x=4
>>> sqrt_x=x**0.5
>>> print(sqrt_x)
2.0
>>> y=5
>>> z=(x+y)**2
>>> print(z)
81
>>> print(x**2+y**2+2*x*y)
81
>>> print("Tell me something...")
Tell me something...
>>> anything = input()
Rajesh
>>> print(anything)
Rajesh
>>> print("Hmm...", anything, "Really")
Hmm... Rajesh Really
>>> lega = float(input("Input First Leg Length"))
Input First Leg Length2.5
>>> legb = float(input("Input Second Leg Length"))
Input Second Leg Length 3.5
>>> hypo = (lega**2 + legb**2)**0.5
>>> print("Hypotenuse=", hypo)
Hypotenuse= 4.301162633521313
>>> lega = float(input("Input First Leg Length"))
Input First Leg Length 4
>>> legb = float(input("Input Second Leg Length"))
Input Second Leg Length 5
>>> print("Hypotenuse=", hypo)
Hypotenuse= 4.301162633521313
>>> hypo = (lega**2 + legb**2)**0.5
>>> print("Hypotenuse=", hypo)
Hypotenuse= 6.4031242374328485
>>> 5*Raj
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    5*Raj
NameError: name 'Raj' is not defined
>>> 5*"Raj "
'Raj Raj Raj Raj Raj '
>>> 5*"2"
'22222'
>>> "rajesh " * 2
'rajesh rajesh '
>>> "rajesh" * -1
''
>>> lega = float(input("Input First Leg Length"))
Input First Leg Length 4
>>> legb = float(input("Input Second Leg Length"))
Input Second Leg Length 3
>>> hypo = str((lega**2 + legb**2)**0.5)
>>> print("hypotenuse=", hypo)
hypotenuse= 5.0
>>> 
