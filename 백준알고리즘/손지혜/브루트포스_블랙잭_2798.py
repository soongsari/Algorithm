from posixpath import split


N, M = map(int,input().split())

arr = list(map(int,input().split()))

min = 300001

for i in range(N):
    for j in range(N):
        if i==j: continue
        for k in range(N):
            if j==k or i==k: continue
            if M - (arr[i]+arr[j]+arr[k]) < min and M - (arr[i]+arr[j]+arr[k]) >=0:
                min = M - (arr[i]+arr[j]+arr[k])


print(M-min)