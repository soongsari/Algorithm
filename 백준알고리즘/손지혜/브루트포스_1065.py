n = int(input())

def isHansu(num):
    res = False
    if len(str(num))<3:
        return True
    else:
        arr = list(map(int,str(num)))
        for i in range(len(arr)):
            val = arr[1]-arr[0]
            if i+1 < len(arr):
                if val != arr[i+1]-arr[i]:
                    break
            if i+1 == len(arr) -1 :
                res = True
    return res

cnt = 0
for i in range(1,n+1):
    if isHansu(i):
        cnt+=1
print(cnt)