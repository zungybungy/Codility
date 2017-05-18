#For a given set of denominations, you are asked to find the minimum number of coins with
#which a given amount of money can be paid.

def greedyCoinChanging(M, k):
    n = len(M)
    result = []
    for i in range(n - 1, -1, -1):
        result += [(M[i], k // M[i])]
        k %= M[i]
    return result

M=[0.1,0.2,0.5,1,2,5]
k=9.8

print(greedyCoinChanging(M, k))
