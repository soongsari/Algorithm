import sys

sudoku = []
blank = []

row = []
col = []
sqr = []

for i in range(9) :
    row.append([j for j in range(1,10)])
    col.append([j for j in range(1,10)])

for i in range(3) :
    temp = []
    for j in range(3) :
        temp.append([j for j in range(1,10)])
    sqr.append(temp)

for i in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

    for j in range(9):
        val = sudoku[i][j]
        if val == 0:
            blank.append(str(i)+str(j))
        else:
            row[i].remove(val)
            col[j].remove(val)
            sqr[i//3][j//3].remove(val)



def bfs(index,slist):


    if index == len(blank):
        for r in slist:
            print(' '.join(map(str, r)))
        exit()

    
    val = blank[index]
    x = int(val[0])
    y = int(val[1])

    interset = (set(row[x]) & set(col[y]) & set(sqr[x//3][y//3]))


    for j in interset:
        slist[x][y]=j
        row[x].remove(j)
        col[y].remove(j)
        sqr[x//3][y//3].remove(j)
        bfs(index+1,slist)
        slist[x][y]=0
        row[x].append(j)
        col[y].append(j)
        sqr[x//3][y//3].append(j)

            
bfs(0,sudoku)