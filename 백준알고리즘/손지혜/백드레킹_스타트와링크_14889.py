import sys
from itertools import combinations

N = int(input())

arr=[]
start = []
link = []

team = set(range(1,N+1))


for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split(" "))))

start = list(combinations(team,N//2))

# def div():
#     if(len(temp)==N//2):
#         if temp not in link:
#             if list(set(t)-set(temp)) not in link:
#                 start.append(temp.copy())
#                 link.append(list(set(t)-set(temp)))
#                 return

#     for i in range(1,N+1):
#         if i not in temp:
#             temp.append(i)
#             div()
#             temp.pop()

# div()

min = 99999999

for i in range(len(start)//2 + 1):
    sumS=0
    sumL=0
    link = list(team - set(start[i]))
    for s in range(N//2):
        for l in range(N//2):
            if s==l:
                continue
            a = start[i][s] -1
            b = start[i][l] -1
            
            c = link[s] -1
            d = link[l] -1

            sumS+= arr[a][b]
            sumL+= arr[c][d]
            
    res = abs(sumS - sumL)
    if min > res:
        min = res

print(min)