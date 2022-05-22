import sys
import collections
N = int(input())

arr=[]
for i in range(N):
    val = int(sys.stdin.readline())
    arr.append(val) 

arr.sort()
cnt = collections.Counter(arr).most_common(2) #최빈값 구하기

print(round(sum(arr)/N)) #첫번째 자리에서 반올림
print(arr[N//2])
if len(cnt) > 1:
    if cnt[0][1]==cnt[1][1]: #가장큰것과 두번째로 큰것의 빈도수가 같으면
        print(cnt[1][0]) #두번째로 큰거 출력
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(abs(arr[N-1]-arr[0]))