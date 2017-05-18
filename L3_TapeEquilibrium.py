# Short Problem Definition:
# Minimize the value |(A[0] + … + A[P-1]) – (A[P] + … + A[N-1])|
def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)

    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)

    return min_dif

A=[3,1,2,4,3]
print(solution(A))