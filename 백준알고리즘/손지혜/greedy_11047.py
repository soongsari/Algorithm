n,k = map(int,input().split())

array = []

index = 0
result = 0

for i in range(n):
    array.append(int(input()))
    if(k>=array[i]):
        index = i


for i in range(index,-1,-1):
    div = k // array[i]
    k -= array[i]*div
    result+=div


print(result)