#Big fishes eat smaller ones
#Need to review this code
def solution(A, B):
    survivals = 0
    stack = []

    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()

            else:
                survivals += 1
        else:
            stack.append(A[idx])

    survivals += len(stack)

    return survivals

A=[4,3,2,1,5] #size of fishes
B=[1,0,0,0,1] #direction of fishes

print(solution(A,B))