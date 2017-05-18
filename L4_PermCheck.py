#PermCheck
#A permutation is a sequence containing each element from 1 to N once, and only once.

def solution(A):
    counter = [0]*len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else:
            if counter[element-1] != 0:
                return 0
            else:
                counter[element-1] = 1

    return 1

A=[3,2,4,1]
print(solution(A))