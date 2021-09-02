def cmb(l):
    r = []
    for i in range(len(l) - 1):
        for y in range(i+1, len(l)):
            s = [l[i], l[y]]
            if s not in r:
                r.append(s)
    return r

print(cmb(["a", "b", "c", "d"]))
