import re

input = input() # 0-8994+8+00-610+722+6691-482+65-3

arr = re.split('([+-])',input)  # 정규식에 괄호까지 넣으면 구분자까지 저장 됌
# ['0', '-', '8994', '+', '8', '+', '00', '-', '610', '+', '722', '+', '6691', '-', '482', '+', '65', '-', '3']

result = "("

for i in range(len(arr)):
    if arr[i]!="+" and arr[i]!="-":
        result += str(int(arr[i]))
    elif arr[i]=="-":
            result+=")-("

    else:
        result += arr[i]

result+=")"

#result : (0)-(8994+8+0)-(610+722+6691)-(482+65)-(3)
print(eval(result))