N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))


for i in range(N):
    cnt=0
    for j in range(N):
        if(i==j):
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt+=1
    print(cnt+1,end=' ')