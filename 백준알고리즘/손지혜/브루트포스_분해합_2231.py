N = input()


if int(N)-len(N)*9 >= 1:
    min = int(N)-len(N)*9
else:
    min = 0


chk = 0

for i in range(min,int(N)+1):
    sum = i
    for val in str(i):
        sum+=int(val)

    if sum == int(N):
        print(i)
        chk = 1
        break

if chk == 0:
    print(0)
