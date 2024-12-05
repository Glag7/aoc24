file =  open("input", "r")

dic = {}
for line in file:
    if (line == "\n"):
        break ;
    nums = line.rstrip().split("|")
    if (nums[0] in dic.keys()):
        dic[nums[0]].append(nums[1])
    else:
        dic[nums[0]] = [nums[1]]

total = 0

for line in file:
    nums = line.rstrip().split(",")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] not in dic[nums[i]]:
                break
        else:
            continue
        break
    else:
        total += int(nums[len(nums) // 2])

print("total is", total)

file.close()
