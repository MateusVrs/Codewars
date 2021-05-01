def solution(s):
    s += '_'
    return [s[p:p+2] for p in range(0, len(s)-1, 2)]
