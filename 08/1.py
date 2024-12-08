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

for nums in dic.values():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            xinc = nums[i][0] - nums[j][0]
            yinc = nums[i][1] - nums[j][1]
            xcur = nums[i][0] + xinc
            if (xcur == nums[j][0]):
                xcur = nums[i][0] - xinc
                ycur = nums[i][1] - yinc
            else:
                ycur = nums[i][1] + yinc
            if (xcur >= 0 and xcur < x and ycur >= 0 and ycur < y):
                pos.append((xcur, ycur))
            xcur = nums[j][0] + xinc
            if (xcur == nums[i][0]):
                xcur = nums[j][0] - xinc
                ycur = nums[j][1] - yinc
            else:
                ycur = nums[j][1] + yinc
            if (xcur >= 0 and xcur < x and ycur >= 0 and ycur < y):
                pos.append((xcur, ycur))

total = len(set(pos))

print("total is", total)

file.close()
