import sys
N = int(input())

arr=[0]*10001 #입력 갯수가 천만개로 메모리 초과를 막기 위해 배열 크기 한정
for i in range(N):
    arr[int(sys.stdin.readline())]+=1 #이부분이 시간초과, 메모리초과 안되도록 하는 핵심

for i in range(len(arr)):
    if arr[i]!=0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i)+'\n') 