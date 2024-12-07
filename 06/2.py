file =  open("input", "r")

i = 0
j = 0
search = 1
s = []
for line in file:
    if (search):
        i += 1
        j = line.find("^") + 1
        if (j):
            search = 0
    s.append("a" + line.rstrip().replace("^", "X") + "a")
s = ["a" * len(s[0])] + s + ["a" * len(s[0])]

total = 0
istart = i
jstart = j
idir = -1
jdir = 0

while (s[i + idir][j + jdir] != "a"):
    new_idir = (jdir == 1) - (jdir == -1)
    new_jdir = (idir == -1) - (idir == 1)

    if (s[i + idir][j + jdir] == "#"):
        idir = new_idir
        jdir = new_jdir
    elif (s[i + idir][j + jdir] == "." or s[i + idir][j + jdir] == "X"):
        if (s[i + idir][j + jdir] == "."):
            idir2 = new_idir
            jdir2 = new_jdir
            i2 = i + idir2
            j2 = j + jdir2
            epic_pos_list = [(i,j, idir, jdir)]
            while (s[i2 + idir2][j2 + jdir2] != "a" and (i2, j2, idir2, jdir2) not in epic_pos_list):
                while (s[i2 + idir2][j2 + jdir2] == "#"):
                    new_idir2 = (jdir2 == 1) - (jdir2 == -1)
                    jdir2 = (idir2 == -1) - (idir2 == 1)
                    idir2 = new_idir2
                while (s[i2 + idir2][j2 + jdir2] in ".X" and (i2, j2, idir2, jdir2) not in epic_pos_list):
                    epic_pos_list.append((i2, j2, idir2, jdir2))
                    i2 += idir2
                    j2 += jdir2
            #if not (i2, j2, idir2, jdir2) in epic_pos_list:
               # for line in s:
                #    print(line)
                #print(epic_pos_list, i2, j2)
            total += (i2, j2, idir2, jdir2) in epic_pos_list

        i += idir
        j += jdir
        stupid_list = list(s[i])
        stupid_list[j] = "X"
        s[i] = "".join(stupid_list)


print("total is", total)

file.close()
