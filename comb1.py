def comb(l):
    r = []
    for i in range(len(l) - 1):
        for y in range(i + 1, len(l)):
            n = [l[i], l[y]]
            if n not in r:
                r.append(n)
    return r

print(comb(["a", "b", "c"]))
