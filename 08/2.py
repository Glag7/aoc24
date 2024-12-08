file =  open("input", "r")

dic = {}
x = 0
y = 0
for line in file:
    y = 0
    for c in line[:-1:]:
        if (c != "."):
            if (c in dic.keys()):
                dic[c].append((x, y))
            else:
                dic[c] = [(x, y)]
        y += 1
    x += 1


pos = []

def epic_line(n1, n2):
    pos.append(n1)
    pos.append(n2)
    xinc = n1[0] - n2[0]
    yinc = n1[1] - n2[1]
    cur = [n1[0] + xinc, n1[1] + yinc]
    if (cur[0] == n2[0]): #shit wrong way
        cur = [n1[0] - xinc, n1[1] - yinc]
        while (cur[0] >= 0 and cur[0] < x and cur[1] >= 0 and cur[1] < y):
            pos.append((cur[0], cur[1]))
            cur[0] -= xinc
            cur[1] -= yinc
    else:
        while (cur[0] >= 0 and cur[0] < x and cur[1] >= 0 and cur[1] < y):
            pos.append((cur[0], cur[1]))
            cur[0] += xinc
            cur[1] += yinc
    cur = [n2[0] + xinc, n2[1] + yinc]
    if (cur[0] == n1[0]): #shit wrong way
        cur = [n2[0] - xinc, n2[1] - yinc]
        while (cur[0] >= 0 and cur[0] < x and cur[1] >= 0 and cur[1] < y):
            pos.append((cur[0], cur[1]))
            cur[0] -= xinc
            cur[1] -= yinc
    else:
        while (cur[0] >= 0 and cur[0] < x and cur[1] >= 0 and cur[1] < y):
            pos.append((cur[0], cur[1]))
            cur[0] += xinc
            cur[1] += yinc

for nums in dic.values():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            epic_line(nums[i], nums[j])

total = len(set(pos))

print("total is", total)

file.close()
