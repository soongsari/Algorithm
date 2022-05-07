n = int(input())

target = (n // 5) * 5
divide5 = n // 5
divide3 = 0
result = -1

if (n == target):
    result = divide5
else:
    if (n - target == 3):
        result = divide5 + 1
    elif (n < 5):
        if n == 3:
            result = 1
    else:
        for i in range(divide5, -1, -1):
            divide3 = (n - (i * 5)) // 3
            if ((n - (i * 5)) % 3 == 0):
                result = i + divide3
                break

print(result)