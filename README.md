# study_for_coding_test


파이썬 코딩테스트
----------
파이썬의 경우 일반적으로 초당 2천만번~1억의 연산이 넘어가면 안된다
완전 탐색, 계수정렬의 경우 일반적으로 100만회 이하의 데이터를 가질 때 사용하는게 적절하다



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
 + 가변인자는 튜플 형태로 전달이 된다
6. 함수의 주석
 + 아래와 같이 return 타입은 ->로 매개변수 타입은 :로 지정 가능 (단!! 어디까지나 주석이기에 강제성은 없다)
```
def funName(x: str, y: float = 6.5) -> int:
    print(type(x))
    print(type(y))
    return x + y

value = funName(3)
출력: 9.5
```
7. if \_\_name\_\_ == '\_\_main\_\_' 의 의미
 + 프로그램의 시작점(entry)인지 확인하기 위함
 + 모듈을 import 해서 사용하는 경우와 모듈내부에서 직접 실행하는경우를 구분하기 위함
 
8. 문자열 관련 함수 
 + isalpha() : 문자열이 영문, 한글인지 확인
 + isnumeric() : 문자열이 숫자인지 확인
 + ''.join(리스트) : 문자열 리스트를 하나의 문자열로 합치는 함수