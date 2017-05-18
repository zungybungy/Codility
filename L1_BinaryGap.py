def solution(N):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2

    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2

    return max_gap


def solution2(N):
    cnt = 0
    result = 0
    found_one = False

    i = N

    while i:
        if i & 1 == 1:
            if (found_one == False):
                found_one = True
            else:
                result = max(result, cnt)
            cnt = 0
        else:
            cnt += 1
        i >>= 1

    return result

print(solution(100))