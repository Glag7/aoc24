file =  open("input", "r")

max_size = 1024 * 16
blink = 25

nums = []
for line in file:
    nums = line[:-1:].split(" ")
    break

for i in range(len(nums)):
    nums[i] = int(nums[i])

total = 0
garbage = {0: nums}

while garbage:
    print("\r", total, end = "", sep = "")
    for i in range(blink, -1, -1):
        if (i in garbage):
            lst = garbage[i]
            l = []
            for j in range(min(len(lst), max_size)):
                ns = str(lst[j])
                nl = len(ns)
                if (lst[j] == 0):
                    l.append(1)
                elif (nl % 2 == 0):
                    l.append(int(ns[:nl // 2:]))
                    l.append(int(ns[nl // 2::]))
                else:
                    l.append(lst[j] * 2024)
            if (i == blink - 1):
                total += len(l)
            elif (i + 1) in garbage:
                garbage[i+1] += l
            else:
                garbage[i+1] = l
            if len(garbage[i]) <= max_size:
                del garbage[i]
            else:
                garbage[i] = garbage[i][max_size::]
            break

print("total is", total)

file.close()
