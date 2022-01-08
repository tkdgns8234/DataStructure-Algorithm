# 1. 선택정렬
# 가장 작은 값을 계속 선택해서 정렬
# 시간복잡도: O(n제곱), 10000개 이상 데이터 다룰 시, 급격히 느려진다.

# 2. 삽입정렬
# 데이터가 거의 정렬되어있을 때 훨씬 효율적이다.
# 선택정렬은 현재 데이터의 상태와 상관없이 무조건 모든원소를 비교하고 교체하지만 삽입 정렬은 다르다.
# 보통은 퀵 정렬보다 느리나, 정렬이 거의 되어있을 땐 퀵정렬보다 빠르기도 하다

# 3. 퀵 정렬
# 시간복잡도 평균 O(NLogN)
# 피벗을 가장 왼쪽으로 삼는 경우 이미 정렬된 경우 비교적 느리게 동작

# 4. 계수 정렬
# 특정 상황에서만 사용할 수 있지만 매우 빠른 정렬알고리즘
# 모든 데이터가 양의 정수이고 N 개, 최댓값이 K 인경우 O(N+K) 복잡도
# => 범위 제한, 정수일때만 사용 가능
# => N 개의 리스트를 선언하고 인덱스에대한 값이 몇개인지 채워가는 방식
# 데이터 크기가 한정되어있고, 동일한값을 가지는 데이터가 여러개존재할때 효율적
# 그게 아니라면 일반적으로 퀵 sort 를 사용

# 파이썬의 sorted, sort 라이브러리는 퀵 sort와 유사한 병합정렬을 사용, 최악의경우 O(NlogN)

# 각 정렬방법을 실제로 구현해보자
# 1. 버블정렬
# array = [2,4,5,1,8,3,9]

# for i in range(len(array)-1, 0, -1):
#     for j in range(i):
#         if array[j] > array[j+1]:
#             array[j],array[j+1] = array[j+1],array[j]

# print(array)
# 2. 선택정렬
# array = [2,4,5,1,8,3,9]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i, len(array)-1):
#         if array[min_index] > array[j+1]:
#             min_index = j+1
#     array[i],array[min_index] = array[min_index],array[i]

# print(array)

# 3.삽입정렬
# else 문 빼먹지 않기!!
# array = [2,4,5,1,8,3,9]

# for i in range(1, len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]
#         else:
#             break;

# print(array)

# 4. 퀵 정렬
# 4-1. 일반적, 직관적 방법
# array = [2,4,5,1,8,3,9]

# def quick_sort(arr, start, end):
#     # 배열이 1 이하인경우 종료
#     if start>=end:
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while left <= right:
#         #left찾고
#         while left <= end and arr[pivot] >= arr[left]:
#             left += 1
#         #right찾고
#         while right >= pivot+1 and arr[pivot] <= arr[right]:
#             right -= 1
        
#         if left > right:
#             arr[pivot],arr[right] = arr[right],arr[pivot]
#         else:
#             arr[left],arr[right] = arr[right],arr[left]
        
#     #재귀
#     quick_sort(arr, start, right-1)
#     quick_sort(arr, right+1, end)

# quick_sort(array,0,len(array)-1)
# print(array)

# 4-2. 파이썬다운 방법

# array = [1,4,7,2,3,9]

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]
    
#     left_side = [i for i in tail if i <= pivot]
#     right_side = [i for i in tail if i >= pivot]
    
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
# print(quick_sort(array))

# 5. 계수정렬
# arr = [1,7,2,9,3,4,2,6]

# count = [0] * (max(arr)+1)

# for i in arr:
#     count[i] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end = " ")

# 연습문제2 위에서 아래로
# n = int(input())

# l = []
# for _ in range(n):
#     l.append(int(input()))

# l.sort(reverse=True)

# for i in range(len(l)):
#     print(l[i], end=" ")

# 연습문제3 성적이 낮은 순서로 학생 출력하기
# 정수, 중복, 성적 관련문제니 계수정렬로 푸는게 적절해보인다
# 계수정렬 말고 데이터 최대 10만개 이니, 내장함수 사용해도됨(시간복잡도 O(nLogn))
# 아직 파이썬 문법에 많이 익숙지않네
# 헷갈렷던점
# 1. 2차원배열 초기화/ 공간만 만들 순 없다 (None 제외)
# 2. input().split() 의 return 은 list // 함수 들어가서 직접 보자 return 이 -> 
# score를 미리 int형으로 형변환하지않은데 아쉬움이있음
# list연산방법 헷갈렸었음 153 line
# None 타입은 len에 잡히지않는다 (에러발생)

# n = int(input())

# #0 ~ 100 점 배열 생성
# score_list = [[None] for i in range(101)]

# for i in range(n):
#     name, score = input().split()
    
#     if score_list[int(score)][0] == None:
#         score_list[int(score)][0] = name
#     else:
#         score_list[int(score)] += [name]

# print(score_list)

# for i in range(len(score_list)):
#     if score_list[i][0] != None:
#         for j in range(len(score_list[i])):
#             print(score_list[i][j])

# 내장함수로 푸는 방법
# key 이용하면 되겠네!

# n = int(input())
# array = []
# for i in range(n):
#     student_info = input().split()
#     array.append((student_info[0], int(student_info[1])))

# array.sort(key=lambda score: score[1])

# for i in array:
#     print(i[0], end=' ')

# 실전문제 4 두 배열의 원소 교체
# 잘 풀었다 근데 하나 틀렸다!
# for 문 안에 조건을 추가하지 않았었다!!
# n, k = map(int, input().split())

# array_a = list(map(int, input().split()))
# array_b = list(map(int, input().split()))

# array_a.sort()
# array_b.sort(reverse=True)

# for i in range(k):
#     if array_a[i] < array_b[i]:
#         array_a[i],array_b[i] = array_b[i],array_a[i]

# print(sum(array_a))