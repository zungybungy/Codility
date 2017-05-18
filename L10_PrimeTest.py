#Different way to test prime
import math
def is_prime(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i += 1
    return True


def is_prime1(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime2(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

print(is_prime(100))