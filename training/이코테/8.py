data = input()

number = 0
rs = []

for i in data:
    if i.isalpha():
        rs.append(i)
    else:
        number += int(i)

rs.sort()

print(''.join(rs) + str(number))