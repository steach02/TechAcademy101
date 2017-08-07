#int variable
num = 1

#string variable
new_str = 'im a string'

#float variable
_float = 0.55

#print with .format
print new_str.title()

# operators

num = 1+1-5*3/2
print num
num +=10
print num
num = 7
print num
num%2
print num

#logical operators and conditionals
# if,or
if num==0 or num ==2:
    print num
# elif,not
elif num not in(new_str):
    print num
# and    
elif num<10 and num>0:
    print num
else:
    print 'what a number'
#while loop
a=True
while a:
    print "hi"
    a=false
#for loop
for letter in "ILovePython":
    print "current letter: "+letter
num = [1,2,3,4,5,]
for number in num:
    print "my number: "+number
myTuple = ("Stephen","James","Teacher")
for _str in my_Tuple:
    print _str+" "
def getStr(_str):
    _str2="your string says "+_str
    return _str2
print getStr("Hello World")

