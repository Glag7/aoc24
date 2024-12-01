file =  open("input", "r")

left = []
right = []
for line in file:
    nums = line.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))
num_dict = dict((n, right.count(n) * left.count(n)) for n in set(left))
total = 0
for num, occ in num_dict.items():
    total += num * occ
print("total is", total)
file.close()
