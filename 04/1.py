def check(s, i, j, iinc, jinc):
    return s[i + iinc][j + jinc] == "M" and s[i + 2 * iinc][j + 2 * jinc] == "A" and s[i + 3 * iinc][j + 3 * jinc] == "S"

file =  open("input", "r")

s = ["a" * 1000]
for line in file:
    s.append("a" + line + "a")
s.append("a" * 1000)

total = 0
for i in range(1, len(s[1]) - 1):
    for j in range(1, len(s) - 1):
        if s[i][j] == 'X':
            total += check(s, i, j, 1, 0)
            total += check(s, i, j, 1, 1)
            total += check(s, i, j, 1, -1)
            total += check(s, i, j, 0, -1)
            total += check(s, i, j, 0, 1)
            total += check(s, i, j, -1, 0)
            total += check(s, i, j, -1, 1)
            total += check(s, i, j, -1, -1)

print("total is", total)

file.close()
