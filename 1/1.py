file =  open("input", "r")

left = []
right = []
for line in file:
    nums = line.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))
left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print("total is", total)

file.close()
