def get_aba(s):
    n = ""
    v = "aeiouAEIOU"
    for ch in s:
        if ch in v:
            n += "aba" + ch.lower()
        else:
            n += ch
    return n

print(get_aba("Cats and Dogs"))
print(get_aba("Aa Bb eE"))
