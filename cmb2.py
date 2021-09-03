def cmb(l):
    r = []
    for i in range(len(l)-1):
        for y in range(i+1, len(l)):
            m = [l[i], l[y]]
            if m not in r:
                r.append(m)
    return r

print(cmb(["a", "b", "c", "d"]))
