# A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
#
# Array A contains only 0s and/or 1s:
#
# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
#
# For example, consider array A such that:
#
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

def solution(A):
    west_cars = 0
    cnt_passings = 0

    for idx in range(len(A) - 1, -1, -1):
        if A[idx] == 0:
            cnt_passings += west_cars
            if cnt_passings > 1000000000:
                return -1
        else:
            west_cars += 1

    return cnt_passings

A=[0,1,1,1,0,0,1]
print(solution(A))