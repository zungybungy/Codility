def solution(X, A):
    passable = [False] * X
    uncovered = X

    for idx in range(len(A)):
        if A[idx] <= 0 or A[idx] > X:
            raise Exception("Invalid value", A[idx])
        if passable[A[idx] - 1] == False:
            passable[A[idx] - 1] = True
            uncovered -= 1
            if uncovered == 0:
                return idx

    return -1

A = [1,3,1,4,2,3,5,4]
print(solution(5,A))