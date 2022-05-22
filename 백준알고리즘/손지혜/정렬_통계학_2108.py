from asyncio.windows_events import NULL
import sys
N = int(input())

arr=[]
cnt=[0]*10000
maxval=0
maxbin=[]
for i in range(N):
    val = int(sys.stdin.readline().rstrip())
    cnt[val+4000]+=1
    if(cnt[val+4000]>maxval):
        maxbin.clear()
        maxbin.append(val)
        maxval=cnt[val+4000]
    elif(cnt[val+4000]==maxval):
        maxbin.append(val)
    arr.append(val) 

arr.sort()
maxbin.sort()

print(round(sum(arr)/N)) #첫번째 자리에서 반올림
print(arr[N//2])
if len(maxbin) == 1:
    print(maxbin[0])
else:
    print(maxbin[1])
print(abs(arr[N-1]-arr[0]))