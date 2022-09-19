data = input()
left = sum(map(int, data[0:len(data)//2]))
right = sum(map(int, data[len(data)//2:]))

if right == left:
    print("LUCKY!")
else :
    print("READY!")