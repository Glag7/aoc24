file =  open("input", "r")

num = []
for line in file:
    num.append([int(n) for n in line.split()])
total = 0
for lst in num:
    err = False
    diff = lst[1] - lst[0]
    if (abs(diff) < 1 or abs(diff) > 3):
        diff = lst[2] - lst[1]
        err = True
    if (abs(diff) < 1 or abs(diff) > 3):
        continue
    i = 1 + err
    while i < len(lst):
        newdiff = lst[i] - lst[i - 1]
        if ((diff < 0) != (newdiff < 0) or abs(newdiff) < 1 or abs(newdiff) > 3):
            if err:
                break
            err = True
            i += 1
            continue
        diff = newdiff
        i += 1
    else:
        total += 1

print("total is", total)

file.close()
