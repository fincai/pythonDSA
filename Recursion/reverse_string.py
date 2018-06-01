def reverse_str(astring):
    if len(astring) == 1:
        return astring
    else:
        return reverse_str(astring[1:]) + astring[0]


print(reverse_str("limit"))
print(reverse_str("follow") == "wollof")
