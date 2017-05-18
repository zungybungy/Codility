#O(N^2)
def quadratic_max_slice(A):
    n = len(A)
    result = 0
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result = max(result, sum)
    return result

#O(N)
def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


A=[4,8,5,6,9]
print(golden_max_slice(A))