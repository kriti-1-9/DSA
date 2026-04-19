def printDuplicates(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for key in freq:
        if freq[key] > 1:
            print(["{}".format(key), freq[key]], end=", ")