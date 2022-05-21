
N,M = map(int,input().split())

arr=[]
for i in range(N):
    arr.append(input())

minval = 100
for x in range(N-7):
    for y in range(M-7):
        cntW = 0
        cntB = 0
        # W가 첫번째
        for i in range(x,x+8):
            for j in range(y,y+8):
                #홀수번째 줄일때
                if i%2==0:
                    #홀수번째 열에 W가 아닌 B가 오면
                    if j%2==0:
                        if arr[i][j] == 'B':
                            cntW+=1
                        else:
                            cntB+=1
                    else: #짝수번째 열에 B가 아닌 W가 오면
                        if arr[i][j] == 'W':
                            cntW+=1
                        else:
                            cntB+=1
                #짝수번째 줄일때
                else:
                    #홀수번째 열에 B가 아닌 W가 오면
                    if j%2==0:
                        if arr[i][j] == 'W':
                            cntW+=1
                        else:
                            cntB+=1
                    else: #짝수번째 열에 W가 아닌 B가 오면
                        if arr[i][j] == 'B':
                            cntW+=1
                        else:
                            cntB+=1
        
        if minval > min(cntW,cntB):
            minval = min(cntW,cntB)

print(minval)

