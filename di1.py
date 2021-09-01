def dger(l,d):
    r = []
    for i in l:
        if i in d:
            r.append(d[i])
        else:
            r.append(i)
    return r

print(dger(['serena', 'lebron', 'messi'], {"lebron":"basketbal","serena":"tennis"}))
