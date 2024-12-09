file =  open("input", "r")

len_line = 0
nums = []
for line in file:
    len_line = len(line) - 1
    for c in line[:-1:]:
        nums.append(int(c))
    break

def sumall(a, b):
    return (b * (b + 1) - a * (a - 1)) // 2

def getpos(lst, i):
    if (len(lst) > i):
        return (sum(lst[:i:]))
    return 0

print(nums)

i = len_line - 1
moved = []
while i > -1:
    for j in range(1, i, 2):
        if (nums[j] >= nums[i]):
            cpy = nums[:j:] + [0, nums[j]]
            if (i == j + 1 and i == len_line - 1):
                pass
            elif (i == j + 1):
                cpy += [nums[j] + nums[i + 1]] + nums[i+2::]
            elif (i == len_line - 1):
                cpy += [nums[j] - nums[i]] + nums[j+1:i-1:]
            else:
                cpy += [nums[j] - nums[i]] + nums[j + 1:i - 1] + [nums[i - 1] + nums[i] + nums[i + 1]] + nums[i + 2::]
            nums = cpy
            print(nums)
            break
    i -= 2

total = 0
pos = 0
for i in range(len(nums)): #calcuer avant
    if (i % 2 == 0):
        total += (i // 2) * sumall(pos, pos + nums[i] - 1)
    pos += nums[i]

print(nums)
print("total is", total)

file.close()
