#it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#there should be an even number of letters;
#there should be an odd number of digits.

def solution(S):
    result = -1
    for word in S.split():
        digits = sum(c.isdigit() for c in word)
        alpha   = sum(c.isalpha() for c in word)
        length = len(word)
        if digits + alpha == length and digits % 2 == 1 and alpha % 2 == 0:
            result = max(result, length)
    return result

S = "test 5 a0A pass007 ?xy1"
print(solution(S))