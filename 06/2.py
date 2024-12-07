#stupid ass brutefoce
def check_cycle(s, i, j, idir, jdir):
    pos_list = []
    while (s[i + idir][j + jdir] != "`" and (i, j, idir, jdir) not in pos_list):
        while (s[i + idir][j + jdir] in "H#"):
            new_idir = (jdir == 1) - (jdir == -1)
            jdir = (idir == -1) - (idir == 1)
            idir = new_idir
        while (s[i + idir][j + jdir] in ".x" and (i, j, idir, jdir) not in pos_list):
            pos_list.append((i, j, idir, jdir))
            i += idir
            j += jdir
    return (i, j, idir, jdir) in pos_list

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
    s.append("`" + line.rstrip().replace("^", "x") + "`")
s = ["`" * len(s[0])] + s + ["`" * len(s[0])]

total = 0
idir = -1
jdir = 0
ogi = i
ogj = j
while (s[i + idir][j + jdir] != "`"):
    while (s[i + idir][j + jdir] == "#"):
        new_idir = (jdir == 1) - (jdir == -1)
        jdir = (idir == -1) - (idir == 1)
        idir = new_idir
    while (s[i + idir][j + jdir] in ".x"):
        i += idir
        j += jdir
        if s[i][j] != "x":
            if (i != ogi or j != ogj):
                stupid_list = list(s[i])
                stupid_list[j] = "H"
                s[i] = "".join(stupid_list) 
                if check_cycle(s, i- idir, j - jdir, idir, jdir):
                    total += 1
        stupid_list = list(s[i])
        stupid_list[j] = "x"
        s[i] = "".join(stupid_list)

print("total is", total)

file.close()
