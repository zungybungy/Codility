#Greates common divisor algorithm by subtraction
def gcd(a, b):
    if a == b:
        return a
    if a > b:
        gcd(a - b, b)
    else:
        gcd(a, b - a)

#Greates common divisor algorithm by dividing
def gcd1(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(10,35))