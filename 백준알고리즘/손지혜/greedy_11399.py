n = input()
data = list(map(int,input().split()))
data.sort()
result = 0

for i in range(len(data)):
    result += data[i]
    result += (len(data)-(i+1))*data[i]

print(result)
