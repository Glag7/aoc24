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

total = 1
idir = -1
jdir = 0
while (s[i + idir][j + jdir] != "a"):
    while (s[i + idir][j + jdir] == "#"):
        new_idir = (jdir == 1) - (jdir == -1)
        jdir = (idir == -1) - (idir == 1)
        idir = new_idir
    while (s[i + idir][j + jdir] == "." or s[i + idir][j + jdir] == "X"):
        i += idir
        j += jdir
        total += (s[i][j] == ".")
        stupid_list = list(s[i])
        stupid_list[j] = "X"
        s[i] = "".join(stupid_list)

print("total is", total)

file.close()
