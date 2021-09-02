def get_aba(s):
    v = "aeiouAEIOU"
    r = ""
    for ch in s:
        if ch in v:
            aba = make_aba(ch)
            r += aba
        else:
            r += ch
    return r

def make_aba(vowel):
    return vowel + "b" + vowel.lower()

print(get_aba("Cats and Dogs"))

