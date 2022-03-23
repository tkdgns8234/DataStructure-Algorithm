# 문제 2. 그룹 단어 체커
# 지문을 잘 읽고 그대로 표현하면 풀 수 있다.
n = int(input())
count = 0
for _ in range(n):
    result = True
    word = input()
    for i in range(0, len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1:]:
                result = False
    if result:
        count += 1
print(count)