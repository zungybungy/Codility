def solution(A):
    result = 0
    for number in A:
        result ^= number

    return result

A=[9,9,3,3,6,6,5,9]
print(solution(A))