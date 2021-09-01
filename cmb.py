def cmb(l):
    r = []
    for i in range(len(l) - 1):
        for y in range(len(l)):
            v = l[i] + l[y]
            if v not in r:
                r.append(v)
    return r

   # return [i + i+1 for i in range(len(l) - 1)]

print(cmb(["a", "b", "c"]))
