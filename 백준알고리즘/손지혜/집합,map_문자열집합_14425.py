import sys
N, M = map(int,input().split())

arrN = {}
for i in range(N):
    arrN[sys.stdin.readline()]=1

cnt = 0
for i in range(M):
    if sys.stdin.readline() in arrN:
        cnt+=1

print(cnt)