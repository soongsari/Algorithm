n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()

next = 0
cnt = 0


i=0
while(i<n):
    j= i+1
    while(j<n):
        if arr[i][1]>arr[j][0]:
            if arr[i][0] != arr[j][0] and arr[i][1] > arr[j][1]:
                next = arr[j][1]
                i = j
        else:
            i = j
            break
        j+=1
    i=j
    cnt+=1


print(cnt)