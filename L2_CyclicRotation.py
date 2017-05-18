def solution(A, K):
    # write your code in Python 2.7
    if len(A) == 0:
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]

A = [3, 8, 9, 7, 6]
print(solution(A,3))