def get_middle(s):
    nl = len(s)//2
    if len(s) % 2 == 0:
        return s[nl-1:nl+1]
    else:
        return s[nl:nl+1]
