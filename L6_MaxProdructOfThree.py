#Max product of 3 in array
def solution(A):
    if len(A) < 3:
        raise Exception("Invalid input")

    A.sort()

    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

A=[-7,8,9,3,-2,1]
print(solution(A))