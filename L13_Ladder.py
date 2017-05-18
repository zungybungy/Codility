#Count the number of different ways of climbing to the top of a ladder.

#We first compute the Fibonacci sequence for the first L+2 numbers. The first two numbers are
# used only as fillers, so we have to index the sequence as A[idx]+1 instead of A[idx]-1.
# The second step is to replace the modulo operation by removing all but the n lowest bits.

def solution(A, B):
    L = max(A)
    P_max = max(B)

    fib = [0] * (L + 2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << P_max) - 1)

    return_arr = [0] * len(A)

    for idx in range(len(A)):
        return_arr[idx] = fib[A[idx] + 1] & ((1 << B[idx]) - 1)

    return return_arr

A=[4,4,5,5,1]
A=[3,2,4,3,1]
solution()