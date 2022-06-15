data = str(input())
answer = []
for i in range(0, len(data)):
    answer.append(data[i:])
answer.sort()
for ans in answer:
    print(ans)
