import sys
N = int(input())

arr = []
for i in range(N):
    x,y = sys.stdin.readline().rstrip().split()
    arr.append((int(x),int(y)))

arr.sort(key=lambda x: (x[1],x[0])) #뒤의 값 오름차순 기준, 뒤의 값이 같으면 앞의 값 오름차순 기준 정렬

for i in range(len(arr)):
    print(arr[i][0],arr[i][1])

