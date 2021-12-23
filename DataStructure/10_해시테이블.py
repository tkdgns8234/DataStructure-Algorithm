# 해시테이블: 매우빠른 평균 삽입,삭제,탐색연산제공

# 중복데이터존재하는경우 느려질수있음 O(N)만큼
# 일반적으로 70% 이상 데이터가 차 있는경우 연산효율느려짐
# collision resolution 을어떤걸사용하는지도 성능 차이가 심함

# table = list    //     hash function       //   collision resolution method 에 따라 해쉬성능좌우됨

# hash function
# division hash func -> % 연산사용