N = int(input())
answer = []
for i in range(N):
    sentence = input().split()
    temp = ''
    for word in sentence:
        temp += (" " + word[::-1])
    answer.append(temp)

for i in answer:
    print(i[1:], sep='\n')