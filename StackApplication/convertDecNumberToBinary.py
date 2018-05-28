import sys
sys.path.append("..")
from pythonds.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    
    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop()) 
        
    return binString

print(divideBy2(42))

def baseConverter(decNumber, base):
    remstack = Stack()
    digits = "0123456789ABCDEF"
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString

print(baseConverter(18, 16))
print(baseConverter(140, 16))
        
