def dik(l,d):
    r = []
    for e in l:
        if e in d:
            r.append(d[e])
        else:
            r.append(e)
    return r

l = ["lebron", "serena", "messi"]
d = { "lebron" : "basketball", "serena" : "tennis", "gretzky" : "hockey" }

print(dik(l,d))
