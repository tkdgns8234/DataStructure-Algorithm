# 힙
# 데이터 확인: O(1) 삽입, 삭제: LogN

# 삽입 시, 힙의 경우 높이가 낮은것부터, 높이가 동일한 경우 왼쪽부터 채워나감
# -> 불균형이 발생하지 않음 늘 균형이 잘맞는 이진트리
# -> 삽입 시 힙의 조건에 만족하지않으면
# 조건에 만족할 떄 까지 부모, 자식노드의 위치를 바꿔나가기만 하면 끝

# 루트노드 삭제: 가장 마지막 요소와 삭제할 요소 교체
# 이후 교체된 루트노드를 좌 우 노드중 작은노드와 계속 교체
