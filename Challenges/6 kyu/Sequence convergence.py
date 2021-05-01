def convergence(n):
    b, ln, lb = 1, [n], [1]
    while True:
        sb, sn = 1, 1
        for e in [b, n]:
            for i in str(e).replace('0', ''):
                sb = sb*int(i) if e == b else sb
                sn = sn*int(i) if e == n else sn
        n += sn
        b += sb
        ln.append(n), lb.append(b)
        if (n in lb):
            return len(ln)-1
        elif (b in ln):
            return len(ln[0:ln.index(lb[-1])])
