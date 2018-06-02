import sys
sys.path.append("..")
from pythonds.stack import Stack

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    remstack = Stack()
    while n > 0:
        remstack.push(convertString[n % base])
        n = n // base
    restr = ""
    while not remstack.isEmpty():
        restr += remstack.pop()
    return restr

print(toStr(18, 16))
print(toStr(1453, 16))
