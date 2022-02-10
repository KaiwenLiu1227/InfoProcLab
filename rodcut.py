def rod_cut(n, p, memo=None):
    c = 0
    if memo is None:
        memo = {0: 0, 1: p[1]}
    if n not in memo:
        bestprice = 0
        for i in range(1, n + 1):
            cutprice = p[i] + rod_cut(n - i, p, memo) -c
            if cutprice > bestprice:
                bestprice = cutprice
        memo[n] = bestprice
    return memo[n]


p = [0, 2, 7, 12, 15, 18, 19, 23, 25, 26, 31]
print(rod_cut(10, p))
