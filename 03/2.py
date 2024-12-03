file =  open("input", "r")

total = 0
do = 1
for line in file:
    line += "aaaaaaaaaa"
    for i in range(len(line)):
        if (line[i:i+4:] == "do()"):
            do = 1
        elif (line[i:i+7:] == "don't()"):
            do = 0
        elif (do and line[i:i+4:] == "mul("):
            end = line[i+4:i+12:].find(")")
            if end != -1:
                numbers = line[i+4:i+4+end:].split(",")
                if (numbers[0].isdigit() and numbers[1].isdigit()):
                    total += int(numbers[0]) * int(numbers[1])

print("total is", total)

file.close()
