file =  open("input", "r")

eq = []
for line in file:
    nums = line.rstrip().split(" ")
    nums[0] = int(nums[0][:-1:])
    for i in range(1, len(nums)):
        nums[i] = int(nums[i])
    eq.append(nums)

def search(wanted, nums):
    if (len(nums) == 1):
        return nums[0] == wanted
    try:
        if (str(wanted).endswith(str(nums[-1])) and search(int(str(wanted)[:-len(str(nums[-1])):]), nums[:-1:])):
            return 1
    except ValueError:
        pass
    mul = wanted // nums[-1]
    if (wanted % nums[-1] == 0 and search(mul, nums[:-1:])):
        return 1
    return search(wanted - nums[-1], nums[:-1:])

total = 0
for nums in eq:
    total += search(nums[0], nums[1::]) * nums[0]
print("total is", total)

file.close()
