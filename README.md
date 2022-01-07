# study_for_coding_test


파이썬 문법 정리
----------
1. ascii 값 <-> 문자
 + chr()
 + ord()
2. 제곱
 + ** 연산자 사용 및 pow() 사용
3. 파이썬의 call by reference 및 call by value
 + 파이썬 자료형은 크게 불변(immutable) 과 가변(mutable)으로 나뉜다.
 + 불변의 경우 call by value
 + 가변의 경우 call by reference 로 동작한다
4. iterable 자료형을 list 형으로 형변환하는 경우 각 요소들이 분리되어 들어간다
 + ex) str = '10110' 
 + print(str)
 + 출력: [1,0,1,1,0]
5. 함수의 매개변수르 *변수이름 형태로 지정하는 경우 가변인자가 된다
 + def test(*args) 선언 시, test(1,2,3,4) 형태로 호출 가능
