file =  open("input", "r")

num = []
for line in file:
    num.append([int(n) for n in line.split()])
total = 0
for lst in num:
    diff = lst[1] - lst[0]
    if (abs(diff) < 1 or abs(diff) > 3):
        continue
    for i in range(2, len(lst)):
        newdiff = lst[i] - lst[i - 1]
        if ((diff < 0) != (newdiff < 0) or abs(newdiff) < 1 or abs(newdiff) > 3):
            break
        diff = newdiff
    else:
        total += 1

print("total is", total)

file.close()
