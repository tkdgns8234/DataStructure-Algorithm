# 2

number = list(map(int, input()))

result = number[0]
for i in number:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)
