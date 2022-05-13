A,B = input().split()

#파이썬은 숫자 무제한이라.. print(A+B)하면 그냥 됌

maxlen = max(len(A),len(B))
A = A.zfill(maxlen+1)
B = B.zfill(maxlen+1)

result =""
mok=0
for i in range(len(A)):
    
    intA = int(A[-i-1]) + mok
    intB = int(B[-i-1])

    mok = int((intA+intB)/10)
    result += str((intA+intB)%10)

    
print(int(result[::-1]))