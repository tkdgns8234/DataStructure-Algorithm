# 신장트리 => 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지않는 부분그래프
# 최소신장트리 => 간선의 합이 최소인 신장트리
# uion-find 이용

# 구현방법
# 1. 간선을 오름차순으로 정렬
# 2. 각 정점이 같은 그룹이라면
# 3. 아무것도 하지 않고 넘어감, 다른 그룹이라면 그룹으로 만든 후 현재선택한 간선을 최소신장트리에 추가
# 4. 간선을 모두 추가했다면 종료 그렇지않다면 그다음 작은 간선을 선택 후 2,3 과정을 반복
