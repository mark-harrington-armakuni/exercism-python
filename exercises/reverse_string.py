def reverse(s):
    r = ""
    i = len(s)
    while i > 0:
        r = r + s[i - 1]
        i -= 1
    return r
