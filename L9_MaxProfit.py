#Given a log of stock prices compute the maximum possible earning.
def solution(A):
    max_profit = 0
    max_day = 0
    min_day = 200000

    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day - min_day)

    return max_profit

A= [23171,21011,21366,21013,21367]
print(solution(A))
