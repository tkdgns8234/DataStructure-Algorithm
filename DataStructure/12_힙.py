# 우선순위 큐를 구현하기 위하여 사용하는 자료구조

# 힙 = 이진트리를 배열로 표현했을 때 꽉 차있는경우를 의미
# 힙의 성질: 부모노드가 항상 자식노드보다 크거나 항상 자식노드보다 작다

# max 힙 -> 부모노드가 항상 자식노드보다 크거나 같다
# 힙의 연산 insert, delete

# insert -> 마지막 위치에 삽입 후 정렬이 필요함
# delete -> delete 위치에 마지막 노드 삽입 후 위에서 아래로 정렬

# find-max -> 상수시간에알수있음
# delete-max -> O(logn) 시간 소요
# insert, delete -> O(logn) 시간에 가능
# O(logn) 의 경우 제곱의 반대라고 생각하면 된다 트리의경우 자식으로 한번씩 이동할떄마다 검사해야할 요소가 /2 만큼 줄어든다

# 힙 시간복잡도

# heapify-down O(h)= O(longn)
# heapify-up   O(h)= O(longn)
# make-heap n, nlogn   //n개 * heapifydown 하면 됨 끝에서부터 리프가 아닌경우 히피파이 다운
# find-max = 상수
# delete-max = logn   //heapify-up하면됨


#결론 힙은 find-max, del-max, insert에 특화되어있음
# 최대최솟값, insert에 특화

# make-heap 과 heap sort는 다르다
# heap sort하는법
# 1. make-heap으로 힙을 만들고
# 2. delete-min과 유사한형태로 정렬 //pop안하고
# delete-min 와 동일한 원리로 pop 하지말고