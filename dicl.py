d = { "banana" : "yellow", "apple" : "red", "mango" : "yellow", "strawberry" : "red" }

def dicl(original):
    reved = {}
    for original_key in original:
        original_value = original[original_key]
        if original_value not in reved:
            reved[original_value] = [original_key]
        else:
            reved[original_value].append(original_key)
    return reved
print(dicl(d))



