#There are N chocolates in a circle. Count the number of chocolates you will eat.

# N and M meet at their least common multiply.
# Dividing this LCM by M gets the number of steps(chocolates) that can be eaten.

def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


def solution(N, M):
    lcm = N * M / gcd(N, M)  # Least common multiple
    return lcm / M


print(solution(13, 2))