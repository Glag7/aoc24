file =  open("input", "r")

nums = []
for line in file:
    l = [-3]
    for c in line[:-1:]:
        l.append(int(c))
    l.append(-3)
    nums.append(l)
nums = [[-3] * len(nums[0])] + nums + [[-3] * len(nums[0])]
pos_list = [[[] for _ in range(len(nums[0]))] for _ in range(len(nums))]

total = 0
for n in range(9, -1, -1):
    for i in range(1, len(nums) - 1):
        for j in range(1, len(nums[0]) - 1):
            if (nums[i][j] == n):
                if n == 9:
                    pos_list[i][j] = [(i, j)] #trust me
                else:
                    if (nums[i + 1][j] == n + 1):
                        pos_list[i][j] += pos_list[i + 1][j]
                    if (nums[i - 1][j] == n + 1):
                        pos_list[i][j] += pos_list[i - 1][j]
                    if (nums[i][j + 1] == n + 1):
                        pos_list[i][j] += pos_list[i][j + 1]
                    if (nums[i][j - 1] == n + 1):
                        pos_list[i][j] += pos_list[i][j - 1]
                if (n == 0):
                    total += len(pos_list[i][j])

print("total is", total)

file.close()
