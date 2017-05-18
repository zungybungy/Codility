def solution(A):
    return len(set([abs(x) for x in A]))

A=[3,2,-6,4,0]
print(solution(A))