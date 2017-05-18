#Find a maximum sum of a compact subsequence of array elements.
def solution(A):
    max_ending = max_slice = -1000000
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)

    return max_slice

A=[3,2,-6,4,0]
print(solution(A))