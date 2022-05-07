n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[1],x[0]))

cnt = 0
end = 0
for i in range(len(arr)):
    if end<=arr[i][0]:
        end = arr[i][1]
        cnt+=1

print(cnt)