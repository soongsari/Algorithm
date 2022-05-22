import sys
N = int(input())

arr = []

for i in range(N):
     val = sys.stdin.readline().rstrip()
     arr.append((len(val),val))

arr = list(set(arr)) #배열 중복제거

arr.sort(key = lambda x : (x[0],x[1]))

for i in range(len(arr)):
    print(arr[i][1])