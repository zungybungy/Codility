#Count the semiprime numbers in the given range [a..b]
def solution(N, P, Q):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= N:
        if (sieve[i]):
            j = i * i
            while j <= N:
                sieve[j] = False
                j += i
        i += 1

    primes = []
    for i in range(2, N + 1):
        if sieve[i]:
            primes.append(i)

    seq = [0] * (N + 1)
    while len(primes) != 0:
        p = primes[0]
        for q in primes:
            if p * q <= N:
                seq[p * q] = 1
            else:
                break
        primes.pop(0)

    for i in range(1, N + 1):
        seq[i] += seq[i - 1]

    res = []
    for i in range(0, len(P)):
        res.append(seq[Q[i]] - seq[P[i] - 1])

    return res

P = [1,4,16]
Q = [26,10,20]
N=26
print(solution(N, P, Q))