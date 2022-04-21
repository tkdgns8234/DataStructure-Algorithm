# 실패
# 행열의 곱셈 방법
# https://mathbang.net/562
# !조건! A * B 일떄 A의 열과 B의 행 갯수가 동일해야한다
# 0행 0열 -> A의 0행 B의 0열을 차례대로 곱한 후 더한 값
# k반복 추가 실패했음

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])): # 공통길이만큼 반복
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))