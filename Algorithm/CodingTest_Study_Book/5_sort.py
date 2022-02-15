# 0. 버블정렬
# 인접한 원소를 계속 비교하고 값을 교체하여 정렬하는 방식
# 한 사이클 마다 맨 뒤 원소가 정해짐
# O(n^2)의 시간복잡도

# 1. 선택정렬
# # 앞에서부터 정렬 맨 앞 원소와 그 뒤 원소를 비교하여 가장 작은 값을 찾는다.
# # 맨 앞 인덱스부터 모든 원소를 계속 비교하여 값을 교체해 나가는 방식
# # swap은 한 싸이클에 한번만 발생
# # 시간복잡도: O(n^2), 10000개 이상 데이터 다룰 시, 급격히 느려진다.

# 2. 삽입정렬
# (0, 1, 2, 3, 4) 1번째 인덱스 원소부터 차례대로 앞의 정렬된 원소와 크기를 비교하며 적절한 위치에 삽입 해 나가는 방식
# 앞에서부터 1개씩 원소가 정렬되며, 정렬된 원소들은 항상 오름차순을 유지하고있는 특징이 있다.

# 보통은 퀵 정렬보다 느리나, 정렬이 거의 되어있을 땐 퀵정렬보다 빠르기도 하다
# 데이터가 거의 정렬되어있을 때 훨씬 효율적이다.
# 일반적으로는 O(n^2)이지만 정렬 된 경우 O(n)까지 시간이 단축된다.

# 3. 퀵 정렬
# 시간복잡도 평균 O(NLogN) 최악O(n^2)
# 파이썬의 경우 피벗 보다작은 부분 + 피벗 + 피벗보다 큰 부분으로
# 나누어 쉽게 구현할 수 있다
# 이미 정렬된 경우 비교적 느리게 동작 O(n^2) 로 동작
# 정렬 할 때마다 피벗의 위치가 가장 앞쪽이나 뒷쪽에 자리잡게 되어있어 분할이 재대로 이루어지지 않는다.
# 대부분의 정렬 알고리즘에서 사용, 정렬된 경우를 대비하여 nlogn을 유지하기 위해 피벗을 설정하는 특정한 규칙을 추가한다
# 피벗을 랜덤하게 설정하거나, 피벗후보를 3개 정해서 3개중의 가운뎃 값으로 설정하거나, 일정 깊이 이상으로 들어가면
# 퀵 소트 대신 nlogn을 보장하는 힙 정렬을 사용한다.
# 피벗을 기준으로 좌, 우 정렬 O(N)
# 정렬해야할 데이터가 2/1 씩 줄어들기때문에 log(n)
# => nlogn

# 병합정렬
# 큰 문제를 작은 문제로 나눈 후 병합 및 정렬하며 문제를 해결
# 분할정복 + 재귀를통해 구현
# 리스트를 각 원소가 1개가될때까지 분할하고
# 분할된 원소를 1 -> 2-> 4 - > 8개 순으로 정렬
# 시간복잡도 nlogn
# (각 원소를 1개가 될떄까지 분할) -> 함수호출횟수 O(n)
# 분할 후 합치는 과정에서 각 줄에서 n 번의 연산이 발생하며 높이가 log n 이기때문에 O(nlogN) 소요
# 퀵정렬과는 다르게 stable sort의 성질을 가지고 있음 (기준값이 같은 경우 본래의 정렬 상태를 유지)

# 기수 정렬 (radix sort)
# 각 요소들을 1의자리 수 부터 배열에 집어 넣은 후 0번째 배열공간부터 값을 하나씩 빼면서
# 모든 자릿수에대해 동일한 연산을 수행
# 자릿수 D 원소의 갯수 N 일 때 시간복잡도 O(DN)


# 4. 계수 정렬
# 특정 상황에서만 사용할 수 있지만 매우 빠른 정렬알고리즘
# 일반적으로 100만 이하의 수 정렬에사용가능
# 모든 데이터가 양의 정수이고 N 개, 최댓값이 K 인경우 O(N+K) 복잡도
# => 범위 제한, 정수일때만 사용 가능
# => N 개의 리스트를 선언하고 인덱스에대한 값이 몇개인지 채워가는 방식
# 데이터 크기가 한정되어있고, 동일한값을 가지는 데이터가 여러개존재할때 효율적
# 그게 아니라면 일반적으로 퀵 sort 를 사용

# 파이썬의 sorted, sort 라이브러리는 퀵 sort와 유사한 병합정렬을 사용, 최악의경우 O(NlogN)

# 각 정렬방법을 실제로 구현해보자
# 1. 버블정렬
# arr = [1,3,2,3,52,67,5,2,4]

# n = len(arr)
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)

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
# 1. 2차원배열 초기화/ 공간만 만들 수도 있다 ex) [[] for i in range(5)]
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