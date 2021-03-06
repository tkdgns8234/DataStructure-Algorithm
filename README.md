# study_for_coding_test


파이썬 코딩테스트
----------
파이썬의 경우 일반적으로 초당 2천만번~1억의 연산이 넘어가면 안된다
완전 탐색, 계수정렬의 경우 일반적으로 100만회 이하의 데이터를 가질 때 사용하는게 적절하다

# 시간 복잡도
1. 4C3 (순서 상관 x) 의 경우 4!/3!(4-3)! 만큼의 시간 소요 (combination)
2. 4P3 (순서가 다른 경우 다른 것으로 판단) 의 경우 4!/(4-3)!만큼의 시간 소요 (permutation)
3. product 의 경우 각각의 list 원소의 갯수만큼 곱해준다
   1. data = ['사과', '배', '귤']
      result = list(product(data, repeat=2))
      의 경우 3**2

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

9. 파이썬의 경우 블록 레벨에서 변수 scope가 달라지지 않는다
```
 if True:
     x = 1
 print(x)
```
 + if 문 블록 안에서 선언한 변수이지만 블록 밖의 영역에서 접근 가능하다

10. 절대값을 구하는 함수
+ abs()

11. 수열 관련 함수
+ 리스트 안에 있는 값들의 모든 조합을 리턴 (다수의 튜플이 반환 됨)
+ combinations(리스트, 수): 순서 상관 없이 출력 (x,y), (y,x) 의 경우 한가지만 생성됨
+ permutations(리스트, 수): 순서를 고려하여 출력 (x,y), (y,x) 의 경우 두 가지 모두 생성
+ product(리스트, 리스트,,리스트,,,): 두 개 이상 리스트의 모든 조합을 구할 때 사용된다. (중복 허용)

12. set 자료형
+ 집합 자료형, 집합에 관련된것을 쉽게처리하기위해 만든 자료형이다
+ 특징: 중복 불가, 순서 없음
+ 중복된 값을 제거할 때 자주 쓰인다, 인덱스접근 시, 순서가 없기때문에 list나 tuple 로 변환이 필요하다

13. 나누기 연산
+ a //= b 를 사용했을 때와 a = int(a/b) 의 연산 결과는 다르다

14. 2차원 배열에서 최댓값 찾기
+ 간단하게 map 을 사용해서 구할 수 있다
+ 사용형태: max(map(max, list))

15. input() 을 sys.stdin.readline() 으로 대체해서 사용하는 경우
+ input().split() 인 경우 개행문자가 포함되지 않으나 (split이 white space를 기준 쪼개서 출력하기 때문)
+ input() 으로 열을 읽어들이는경우 개행 문자가 포함됨에 유의하자

16. Immutable과 Mutable
+ 파이썬에서는 변경 불가능한 객체(해당 객체의 주솟값을 변경할 수 없는)를 Immutable 하다 라고 한다.
  + int, float, string, bool 등 기본자료형, tuple
  + call by value 처럼 동작
  + 새로운 값을 대입하면 객체가 새로 생성됨
+ 수정이 가능한 객체
  + list, dict, 사용자 정의 클래스 등
  + call by reference 처럼 동작
  

17. 파이썬의 * (asterisk)란?
+ *를 단독으로 사용하는 경우 -> 언패킹(unpacking)
  + 함수의 파라미터로 사용되는 *args 는 args로 들어오는 리스트나 튜플같은 객체를 언패킹하는것과 동일함
  + tuple 형태로 데이터가 들어옴
+ **
  + 함수의 파라미터로 사용되는 **kewards 는 사전자료형을 사용할때 사용

18. Counter
+ 파이썬 collections의 Counter 클래스
+ c = Counter([]) 형태로 사용
+ 키:값 형태의 딕셔너리 생성하는 함수