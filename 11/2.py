file =  open("input", "r")

nums = []
for line in file:
    nums = line[:-1:].split(" ")
    break

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(75):
    print(i)
    l = []
    for n in nums:
        ns = str(n)
        nl = len(ns)
        if (n == 0):
            l.append(1)
        elif (nl % 2 == 0):
            l.append(int(ns[:nl // 2:]))
            l.append(int(ns[nl // 2::]))
        else:
            l.append(n * 2024)
    nums = l 

total = len(nums)
print("total is", total)

file.close()
