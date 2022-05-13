T = int(input())


arr = [[0]*15 for i in range(15)]

for i in range(0,15):
    sum = 0
    for j in range(1, 15):
        if i==0: 
            arr[i][j] = j
        else:
            sum+= arr[i-1][j]
            arr[i][j] = sum

for i in range(T):
     k = int(input()) 
     n = int(input())
     print(arr[k][n])


