#Counting possible triangles in array - A+B >C
def solution(A):
    A.sort()
    print( A)
    triangle_cnt = 0

    for P_idx in range(0, len(A) - 2):
        Q_idx = P_idx + 1
        R_idx = P_idx + 2
        while (R_idx < len(A)):
            if A[P_idx] + A[Q_idx] > A[R_idx]:
                triangle_cnt += R_idx - Q_idx
                R_idx += 1
            elif Q_idx < R_idx - 1:
                Q_idx += 1
            else:
                R_idx += 1
                Q_idx += 1

    return triangle_cnt

A=[3,2,9,4,0]
print(solution(A))