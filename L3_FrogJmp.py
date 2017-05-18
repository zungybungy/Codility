#Short Problem Definition:
#Count minimal number of jumps from position X to Y.

def solution(X, Y, D):
    if Y < X or D <= 0:
        raise Exception("Invalid arguments")

    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return ((Y - X) // D) + 1


print(solution(10,85,30))