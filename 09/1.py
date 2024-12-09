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

total = 0
i = 0
j = len(nums) - 1
pos = 0
empty = 0
while i < j:
    if (empty == 0 and i % 2 == 0):
        total += (i // 2) * sumall(pos, pos + nums[i] - 1)
        pos += nums[i]
        i += 1
    elif empty == 0:
        empty = nums[i]
        i += 1
    elif (j % 2 == 1):
        j -= 1
    elif (empty >= nums[j]):
        total += (j // 2) * sumall(pos, pos + nums[j] - 1)
        pos += nums[j]
        empty -= nums[j]
        j -= 1
    else:
        total += (j // 2) * sumall(pos, pos + empty - 1)
        pos += empty
        nums[j] -= empty
        empty = 0
if empty:
    total += (j // 2) * sumall(pos, pos + empty - 1)
    pos += empty
    nums[j] -= empty
total += (i // 2) * sumall(pos, pos + nums[i] - 1)

print("total is", total)

file.close()
