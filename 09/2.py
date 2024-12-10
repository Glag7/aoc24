file =  open("input", "r")

len_line = 0
nums = []
for line in file:
    len_line = len(line) - 1
    for i in range(len_line):
        if (i % 2 == 0):
            nums.append((int(line[i]), i // 2))
        else:
            nums.append((int(line[i]), -1))
    break

def sumall(a, b):
    return (b * (b + 1) - a * (a - 1)) // 2

i = len_line - 1
while i > -1:
    if (nums[i][1] <= i // 2):
        for j in range(1, i, 2):
            if (nums[j][0] >= nums[i][0]):
                cpy = nums[:j:] + [(0, -1), (nums[i])]
                if (i == j + 1 and i == len_line - 1):
                    pass
                elif (i == j + 1):
                    cpy += [(nums[j][0] + nums[i + 1][0], -1)] + nums[i+2::]
                elif (i == len_line - 1):
                    cpy += [(nums[j][0] - nums[i][0], -1)] + nums[j+1:i-1:]
                    i += 2
                else:
                    cpy += [(nums[j][0] - nums[i][0], -1)] + nums[j + 1:i - 1:] + [(nums[i - 1][0] + nums[i][0] + nums[i + 1][0], -1)] + nums[i + 2::]
                    i += 2
                nums = cpy
                break
    i -= 2

total = 0
pos = 0
for i in range(len(nums)):
    if (i % 2 == 0):
        total += nums[i][1] * sumall(pos, pos + nums[i][0] - 1)
    pos += nums[i][0]

print("total is", total)

file.close()
