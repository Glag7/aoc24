file =  open("input", "r")

i = 0
j = 0
search = 1
s = ["a" * 1000]
for line in file:
    if (search):
        i += 1
        j = line.find("^") + 1
        if (j):
            search = 0
    s.append("a" + line.rstrip().replace("^", "X") + "a")
s.append("a" * 1000)

istart = i
jstart = j
total = 0
idir = -1
jdir = 0
while (s[i + idir][j + jdir] != "a"): 
    new_idir = (jdir == 1) - (jdir == -1)
    new_jdir = (idir == -1) - (idir == 1)
    while (s[i + idir][j + jdir] == "#"):
        idir = new_idir
        jdir = new_jdir
    new_idir = (jdir == 1) - (jdir == -1)
    new_jdir = (idir == -1) - (idir == 1)
    while (s[i + idir][j + jdir] == "." or s[i + idir][j + jdir] == "X"):
        if (s[i + new_idir][j + new_jdir] == "X" and (i != istart or j != jstart)):
            i2 = i + new_idir
            j2 = j + new_jdir
            while (s[i2][j2] == "X"):
                i2 += new_idir
                j2 += new_jdir
            total += s[i2][j2] == "#"
        i += idir
        j += jdir
        stupid_list = list(s[i])
        stupid_list[j] = "X"
        s[i] = "".join(stupid_list)

for line in s:
    print(line)
print("total is", total)

file.close()
