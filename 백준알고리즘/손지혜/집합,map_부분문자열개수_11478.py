S = input()

arr = []
for i in range(len(S)):
    for j in range(i,len(S)):
        arr.append(S[i:j+1])

print(len(set(arr)))