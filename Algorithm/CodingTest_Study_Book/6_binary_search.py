# 순차 탐색은 최악의 경우 O(n)의 시간이 소요됨

# 이진 탐색
# 이진 탐색은 데이터가 정렬되어있는경우에만 사용할 수 있다.
# 구현 방법: start, end, target을 이용해 구현
# 데이터 범위를 절반씩 좁혀가며 탐색하기에 시간복잡도는 O(logN)

# 파이썬의 set 자료형을 사용하는 경우, 내부적으로 해시테이블 형태의 구조를 사용하기때문에
# 탐색 시간이 O(1)이 될 수 있다. ex) ~ in set

# 큰 데이터를 사용하는경우 대부분 트리 , 이진탐색구조 사용 (ex) db)

# 이진탐색 구현 재귀
# array = [1,2,6,7,11,13,16,18,21,32,64,223]

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end)//2
    
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)


# result = binary_search(array, 18, 0, len(array)-1)

# if result == None:
#     print("찾고자 하는 값이 없습니다")
# else:
#     print("해당 값은 %d 위치에 존재합니다" % result + 1)


# 이진탐색 구현 반복문
# array = [1,2,6,7,11,13,16,18,21,32,64,223]

# def binary_search(array,target,start,end):
#     while start <= end:
#         mid = (start+end)//2
        
#         if array[mid] == target:
#             return mid + 1
#         elif array[mid] < target:
#             start = mid + 1
#         elif array[mid] > target:
#             end = mid - 1
#     return None

# result = binary_search(array,32,0,len(array)-1)
# if result != None:
#     print("%d 번째 위치에 값이 존재합니다." % result)
# else:
#     print("값이 존재하지 않습니다")

# 실전문제 2 부품 찾기
# 안타깝게 틀렸어
# 이진탐색의 조건 데이터가 정렬되어있어야 함을 간과했음 sort() 추가
# set() 자료형으로도 풀  수 있다. (해시테이블 구조) 삽입 삭제 탐색 O(1)
# import sys

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+end)//2
        
#         if array[mid] == target:
#             return target
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#     return None

# n = int(input())
# nl = list(sys.stdin.readline().rstrip().split())
# nl.sort()

# m = int(input())
# ml = list(sys.stdin.readline().rstrip().split())

# for i in ml:
#     if binary_search(nl,i,0,len(nl)-1) != None:
#         print("yes", end= " ")
#     else:
#         print("no", end=" ")

# 실전문제 3 떡볶이 떡 만들기
#-----------------------------------------------
# import sys

# n, m = map(int, input.split())
# l = list(sys.stdin.readline().rstrip().split())

# def binary_search(array, target, start, end):
#     if start < end:
#         mid = (start+end)//2
#         sum = 0
#         for i in array:
#             if (i - mid) > 0:
#                 sum += (i-mid)
                
#         if sum > target:
#             binary_search(array, target, mid+1, end)
#         elif sum < target:
#             binary_search(array, target, start, mid-1)

# binary_search(l, m, 0, 1e9)
# 위 코드에서 포기했는데
# 일부 실수를 제외하면 그냥 다 한거였어
# 키포인트는 이진탐색은 진행되면 진행될수록 정답에 가까워진다는거야 무한으로 진행되지 않는다는말이지
# 아래 코드가 정답에가깝다 함수화 굳이 안하는게 코드가 더 깔끔하긴하네

# import sys

# n, m = map(int, input().split())
# l = list(map(int, sys.stdin.readline().rstrip().split()))

# def binary_search(array, target, start, end):
#     result = 0
#     while start <= end:
#         sum = 0
#         mid = (start+end)//2
#         for i in array:
#             if (i - mid) > 0:
#                 sum += (i-mid)
#         if sum >= target: # 이부분 매우 헷갈렸음 값이 같을때도 result를 기록해야지 당연히 =를 빼먹었었다..
#             result = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return result

# result = binary_search(l, m, 0, max(l))
# print(result)
#-----------------------------------------------