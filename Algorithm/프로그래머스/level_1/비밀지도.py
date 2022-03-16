def fill(answer, arr, n):
    for i, num in enumerate(arr):
        row = str(bin(num)[2:]).rjust(n, '0')
        for j, num2 in enumerate(row):
            if num2 == '1':
                answer[i][j] = '#'

def solution(n, arr1, arr2):
    answer = [[" "]*n for i in range(n)]
    fill(answer, arr1, n)
    fill(answer, arr2, n)
    answer = list(map("".join, answer))
    return answer


# 좋은 코드
# bit 연산, zip 사용
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer