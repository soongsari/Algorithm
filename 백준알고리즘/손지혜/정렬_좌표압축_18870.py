N = int(input())
arr = list(map(int,input().split()))
arrset = list(set(arr))

arrset.sort()

arrmap = {} #딕셔너리(hashmap같음)
for i in range(len(arrset)):
    arrmap[arrset[i]] = i # key, value값으로 저장

for i in range(N):
    print(arrmap[arr[i]],end=' ')