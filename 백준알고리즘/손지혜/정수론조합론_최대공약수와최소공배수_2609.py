
T = int(input())
for i in range(T):
    A,B = map(int,input().split())

    Big = max(A,B)
    Small = min(A,B)

    while(Big%Small!=0):
        Big, Small= Small, Big%Small

    #print(Small) #최대공약수
    print((A*B)//Small) #최소공배수 = 두수곱하기//최대공약수