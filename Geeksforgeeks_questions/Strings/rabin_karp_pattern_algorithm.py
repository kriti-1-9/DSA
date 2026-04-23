def search(pat, txt):
    d = 256
    q = 101
    m = len(pat)
    n = len(txt)
    p = 0
    t = 0
    h = 1
    ans = []
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                ans.append(i)
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if t < 0:
                t += q
    return ans