import sys
N = int(input())

arr = []

for i in range(N):
     age, name = sys.stdin.readline().split()
     arr.append((int(age),name))  # int 빼먹지 않게 주의해야 함

arr.sort(key = lambda x : (x[0]))  # 1개를 기준으로 정렬 시, 뒤의 순서는 입력된 순서 유지해서 정렬 됌

for i in range(len(arr)):
    print(arr[i][0],arr[i][1])