#Find the minimal positive integer not occurring in a given sequence.
def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value - 1] = True

    for idx in range(len(seen)):
        if seen[idx] == False:
            return idx + 1

    return len(A) + 1

A=[3,2,4,1,6]
print(solution(A))