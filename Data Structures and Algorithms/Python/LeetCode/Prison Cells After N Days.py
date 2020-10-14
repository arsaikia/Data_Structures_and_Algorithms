def prisonAfterNDays(cells, N):
    seen = {str(cells): N}
    while N:
        seen.setdefault(str(cells), N)
        N -= 1
        cells = [0] + [cells[i - 1] ^ cells[i + 1]
                       ^ 1 for i in range(1, len(cells) - 1)] + [0]
        if str(cells) in seen:
            N = N % (seen[str(cells)] - N)
    return cells


cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 192
print(prisonAfterNDays(cells, n))
