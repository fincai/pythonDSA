num2char = "0123456789ABCDEF"

def toStr(n, base): 
    if n < base:
        return num2char[n]
    else:
        return toStr(n // base, base) + \
               num2char[n % base]

print(toStr(18, 16))
print(toStr(1453, 16))
