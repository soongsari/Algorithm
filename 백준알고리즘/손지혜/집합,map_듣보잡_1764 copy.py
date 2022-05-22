import sys
N, M = map(int,input().split())

arrN = {}
for i in range(N):
    arrN[sys.stdin.readline().rstrip()]=1

cnt = 0
result=[]
for i in range(M):
    val = sys.stdin.readline().rstrip()
    if val in arrN:
        cnt+=1
        result.append(val)

result.sort()
print(cnt)
for i in result:
    print(i)