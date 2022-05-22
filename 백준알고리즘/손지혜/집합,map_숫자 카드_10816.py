N = int(input())
arr = list(map(int,input().split()))
dic = {}
for i in range(N):
    if arr[i] in dic:
        dic[arr[i]] = dic[arr[i]] + 1
    else:
        dic[arr[i]] = 1

M = int(input())
arr = list(map(int,input().split()))

for i in range(M):
    if arr[i] in dic:  #키가 존재하냐
        print(dic[arr[i]],end=' ')
    else:
        print(0,end=' ')
