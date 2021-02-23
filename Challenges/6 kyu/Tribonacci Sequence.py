def tribonacci(seq, n):
    for v in range(n-3):
        seq.append(sum(seq[v:v+3]))
    return seq[:n]
