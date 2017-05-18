#Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K )) // K

print(solution(2,100,2))