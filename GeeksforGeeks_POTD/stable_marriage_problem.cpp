def stableMarriage(n, men, women):
    wife = [-1] * n
    husband = [-1] * n
    next_proposal = [0] * n

    # ranking[w][m]
    ranking = [[0]*n for _ in range(n)]
    for w in range(n):
        for i, m in enumerate(women[w]):
            ranking[w][m] = i

    free_men = list(range(n))

    while free_men:
        m = free_men.pop(0)
        w = men[m][next_proposal[m]]
        next_proposal[m] += 1

        if wife[w] == -1:
            wife[w] = m
            husband[m] = w
        else:
            m2 = wife[w]
            if ranking[w][m] < ranking[w][m2]:
                wife[w] = m
                husband[m] = w
                husband[m2] = -1
                free_men.append(m2)
            else:
                free_men.append(m)

    return husband