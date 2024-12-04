file =  open("input", "r")

s = ["a" * 1000]
for line in file:
    s.append("a" + line + "a")
s.append("a" * 1000)

total = 0
for i in range(1, len(s[1]) - 1):
    for j in range(1, len(s) - 1):
        if s[i][j] == 'A':
            total += ((s[i + 1][j + 1] == "S" and s[i - 1][j - 1] == "M") or (s[i + 1][j + 1] == "M" and s[i - 1][j - 1] == "S")) \
                    and ((s[i - 1][j + 1] == "S" and s[i + 1][j - 1] == "M") or (s[i - 1][j + 1] == "M" and s[i + 1][j - 1] == "S"))

print("total is", total)

file.close()
