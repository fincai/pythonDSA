def gcd(m, n):
    while m % n != 0:
        r = m % n
        m = n
        n = r
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(str(self.num), '/', str(self.den))
        
    def __add__(self, otherFraction):
        newnum = self.num * otherFraction.den + \
                 self.den * otherFraction.num
        newden = self.den * otherFraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum


x = Fraction(1, 2)
y = Fraction(1, 4)
print(x+y)
print(x == y)
