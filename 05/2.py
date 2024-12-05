file =  open("input", "r")

dic = {}
for line in file:
    if (line == "\n"):
        break ;
    nums = line.rstrip().split("|")
    if (int(nums[0]) in dic.keys()):
        dic[int(nums[0])].append(int(nums[1]))
    else:
        dic[int(nums[0])] = [int(nums[1])]

total = 0

for line in file:
    nums = line.rstrip().split(",")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if int(nums[j]) not in dic[int(nums[i])]:
                break
        else:
            continue
        break
    else:
        continue
    i = 0
    while i < len(nums):
        j = i + 1
        while (j < len(nums)):
            if int(nums[j]) not in dic[int(nums[i])]:
                skibidi = nums[i]
                nums[i] = nums[j]
                nums[j] = skibidi
                break
            j += 1
        else:
            i += 1
    total += int(nums[len(nums) // 2])

print("total is", total)

file.close()
