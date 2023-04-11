# 정수형 실수형 복소수형

- 정수형

```python
a = 1000
print(a)
```

- 실수형(소수점 아래의 데이터를 포함하는 수 자료형)

```python
a = 5.
print(a) // 5.0
```

-> 지수 표현 방식 (유효 숫자e 지수 = 유효숫자 \*10 지수)
-> 지수 표현 방식은 실수로 처리된다.

## 수자료형의 연산

1. 파이썬에서 나누기 연산자는 나눠진 결과를 실수형으로 반환한다.
2. 파이썬에서는 몫 연산자가 있다. (//)

- 복소수형

# 리스트

여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형이다.
리스트가 굉장히 강력하다. 일반적인 배열에 이어 연결 리스트의 속성을 제공한다.

## 리스트 초기화

list() 혹은 []로 초기화해야한다.

```python
a = [0] * n
[0,0,0,0,0 ...]
```

자바스크립트에선 Array.from({},) 이런식으로 했는데

## 슬라이싱

슬라이싱을 제공한다. 연속적인 위치의 값
자바스크립트에서 slice와 동일!!!

```python
a = [1,2,3,4]
print(a[1:4]) // 2,3,4
```

## 리스트 컴프리헨션

내부적으로 반복문과 조건문을 포함할 수 있다.

```python
a = [i for i in range(20) if i % 2 == 1]

print(a)

a = [i * i for i in range(1,10)]

print(a)
```

리스트 컴프리헨션은 2차원 리스트를 초기화할때 효과적으로 사용될 수 있다.
특히 N\*M 크기의 2차원 리스트를 한번에 초기화 해야할때 유용하다

### 언더바 사용 이유

반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 언더바를 사용한다

```python
for _ in range(5):
  print("Hello world")
```

![[스크린샷 2023-04-09 오후 8.54.29.png|500]]
append() : 가장 뒤에 요소 하나를 추가할때 사용한다. O(1)
sort() : O(nlogn)
reverse() : O(n)
insert() : O(n)
count() : 특정 값을 가지는 데이터의 수를 셀때 매소드 O(n)
remove() : 특정 값을 제거하는데 사용된다. 만약 여러개가 있다면 한개만 제거하는 특징이 있다. O(n)

# 문자열 튜플

- 문자열
  "", ' '은 js랑 동일하다
  js에서 변수를 넣을 수 있게 하는 기호는 파이썬에서는 뺵슬래쉬 같다

### 문자열 연산

- 덧셈
  -> 문자열끼리 더하면 문자열이 더해진다
- 곱셈
  -> 양의 정수와 곱하면 정수만큼 문자열이 길어진다.

### 문자열 포매팅

```js
const number = 21;
const test = `my age is ${number}`;
```

```python
# 문자 포맷팅
## 숫자 바로 대입
print("I eat %d apples" % 3)

## 문자열 바로 대입
print("I eat %s apples" %"five")

## 2개 이상 대입
number =10
day = "three"
print ("I ate %d apples. so i was sick for %s days" %(number , day))


## format 함수로 포매팅
print("I eat {0} apples".format("three"))
print("I eat {0} apples during {1}days".format("three", 3))


## 공백 채우기
print("{0:=^10}".format("hi"))
```

이런식으로 문자열안에 변수를 삽입했는데 파이썬에서는 약간 다른 것 같다. 어제는 print(f)이 동일한 개념이겠거니 했으나 다르다는 것을 오늘 알게 됐다.

### 문자열 내장 함수

1. count : 특정 문자열과 동일한 문자열의 갯수 반환
2. find : 특정 문자열의 첫 인덱스 반환 없으면 -1
3. index : find와 동일하지만 반환이 없으면 에러 발생시킴
4. join : 문자열 삽입
5. upper() : 대문자로
6. lower(): 소문자로
7. lstrip() : 왼쪽 공백 없애기
8. rstrip() : 오른쪽 공백 없애기
9. replace() : 문자열 바꾸기
10. split() : 문자열 나누기

# 튜플

리스트와 유사하지만 한번 선언된 값을 변경할 수 없다는 특징이 있다. (문자열과 동일한 원리 )
리스트는 대괄호 튜플은 소괄호를 이용한다
튜플은 리스트보다 기능이 제한적이어서 공간이 효율적이다.

### 사용처

1. 서로 다른 성질의 데이터를 묶어 사용할떄 (최단경로에서 비용을 실수 , 노드번호는 정수형으로 )
2. 데이터의 나열을 해싱의 키 값으로 사용해야 할때
3. 튜플은 변경이 불가해서 리스트와 다르게 키 값으로 사용될 수 있다.

# 사전 자료형

==js의 map()과 동일==
key와 value로 이루어진 쌍 (순서가 정해지지 않는다.)
파이썬은 사전 자료형 자체가 hash Table로 이루어져있어 데이터 조회, 수정에서 O(1)의 성능을 보인다.

```python
data = dict()

data['사과'] = 'Apple'

print(data)

if '사과' in data:
  print('사과를 키로 가지고 있어요')
```

- 키와 value를 각각 뽑아내기 위해 매소드를 지원한다
  키는 keys() 값 데이터는 values()

# 집합 자료형

==js의 set()과 동일==
중복을 허용하지 않는다.
순서가 없다.

```python
data = set([1,1,1,1,2,3,4,4])

print(data)

data = {1,1,1,1,1,1,2}

print(data)
```

## 연산 제공

합집합 : |
교집합 : &
차집합 : -

## 추가, 삭제 메소드

add
update() : 여러개 추가
remove()

### 튜플과 리스트와의 사전, 집합 자료형의 차이

순서가 없기에 인덱싱으로 접근이 불가하고 key 값으로 접근할 수 있다는 것.
입력은 input()으로
출력은 print()
print(f)는 js의 백스트링과 같다!!

# 조건문

조건문이란 흐름을 제어하는 문법.

자바스크립트에선

```js
if() {
} else if() {

} else {}
```

python 에선

```python
if 조건문 1:
	조건문이 참일때 실행되는 코드
elif 조건문 2:
	조건문 1에 해당하지 않고, 조건문 2가 true
else:
	나머지에 부합하면 실행하는 코드
```

> 오호 파이썬이 조금 더 가독성이 좋은 것 같다.

## 연산자

### 비교 연산자

자바스크립트와 동일하지만 js의 === 의 기능이 없다

### 논리 연산자

1. X and Y === js 의 &&
2. X or Y === js 의 ||
3. not X === js 의 !
   뭔가 더 영어같다는 느낌을 받는다. 좋다.
4. in 연산자와 not in 연산다 === js 에서도 객체 안에 해당 키값을 찾을때 in 을 사용했는데 동일하다고 생각된다. 여기서는 리스트, 튜플, 사전 자료형에서 쓴다.

### 기타 연산자

1. 조건문 안에서 pass === js continue와 비슷하다.
2. 실행될 소스코드가 한줄이면 조건문 안에서 줄바꿈을 하지 않아도 된다.

```python
if score = 80: result = 'Success'
```

3. 조건부 표현식을 사용하면 더 간결하게 사용할 수 있다(약간 js의 삼항연산자같은건가?)
   -> 뭔가 값으로 사용할 수 있는 것으로 보아 삼항과 동일한 기능을 하는 것 같다.

```python
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)
```

4. js에서 부등식을 and(&&)나 or (||)로 엮여 사용하는게 불편했는데 python에서는 수학의 부등식을 그대로 사용할 수 있다고 한다.

```python
x = 15
if 0 < x < 20
	print("x는 0이상 20 미만의 수입니다.")
```

# 반복문

특정한 소스코드를 반복적으로 실행하고자 할때 사용할 수 있다.

- for 문 (상대적으로 소스코드가 짧게 나온다.)
- while 문

## while 문

조건문이 참일 때에 한해서 반복적으로 코드가 수행되는 문

```python
i = 1
result = 0

while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

```

## for 문

리스트를 사용하는 대표적인 구조

```python
for variable in list :
	source code

result = 0

for i in range(1, 10):
	result += i
print(result)

# js에서는

for( let i = 0; i < list.length; i ++ ){
	sourceCode()
}

```

확실히 Js보다 더 간단한 것 같다.

### 특징

1. range()의 값으로 하나의 값만 넣으면 시작 index는 자동으로 0.
2. range(start, end) 두개의 값을 넣으면 start index 부터 end -1 Index까지 반복된다.

# 함수

동일한 코드를 반복적으로 사용하지 않기 위해 재사용하는 하나의 방식인 함수

```python
def 함수명(매개변수):
	실행할 소스코드
	return 반환 값
```

- 파이썬에서는 함수를 호출하는 과정에서 인자를 파라미터의 변수에 직접 지정할 수 있다.

```python
def add(a,b):
    return a + b

add(b = 1, a = 4)

```

- 전역 변수에 대한 참조를 global이라는 키워드로 하는구나?
  (js는 scope chaning으로 자동적으로 상위 스코프를 검색하는데 파이썬은 다르구나? )

```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print('global',a)
```

## 람다 표현식

함수를 간단하게 작성하는 일련의 방법

# 입력

## 한 줄의 문자열을 입력

input()

## 여러 개의 데이터를 입력(공백으로 구분)

```python
list(map(int, input().split()))
```

여러개의 데이터를 공백으로 나눈 배열로 바꾼 뒤, map을 이용해서 해당 배열의 모든 원소에 int() 함수를 맵핑하는 것. 최종적으로 그 결과물을 list()로 감싸주어 입력받은 문자열을 띄어쓰리고 구분하여 각각 숫자 자료형으로 저장하게 되는 것.

## 입력을 빠르게 받아야 할때 (정렬, 이진탐색, 최단 경로)

sys 라이브러리 사용

```python
import sys
sys.stdin.readline().rstrip()
```

# 출력

자바스크립트 백틱과 같이 변수와 함께 사용하는 방법은 파이썬에서는 print(f{})이다.

# 핵심 라이브러리

1. **내장 함수**

   1. input()
   2. print()
   3. min() :최솟값
   4. max( one , two or more)
   5. sorted() or sorted([1,2,3,] , reverse =True)
   6. 리스트와 같은 iterable 객체는 기본적으로 sort() 내장 매소드를 가지고 있다.

2. **itertools** : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공한다.
   1. permutations : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (순열)을 계산
   2. combinations : 조합
   3. product : 모든 경우 순열 계산 원소를 중복하여 뽑는다.
3. **heapq** : 힙 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용된다.
   1. 원소 삽입 : heapq.heappush()
   2. 원소 제거 : heapq.heappop()
4. **bisect** : 이진 탐색 기능을 제공하는 라이브러리

   1. bisect_left() (OlogN)
   2. bisect_right() (OlogN)

   ```python
   from bisect import bisect_left, bisect_right

   a = [1,2,4,4,8]
   x = 2

   print(bisect_left(a,x))
   print(bisect_right(a,x))
   ```

5. **collections** : 덱 , 카운터등의 유용한 자료구조를 포함하고 있는 라이브러리

   1. deque
      - 파이썬에서는 디큐를 활용해서 큐를 구현한다고 한다. js에서는 기본 내장 매소드인 pop(), push()를 활용해서 구현했었는데.
      - 파이썬에서 append와 pop 매소드는 리스트 가장 뒤에 있는 원소를 기준으로 추가하고 삭제한다. 그래서 가장 앞에 있는 원소를 처리할때 시간 복잡도는 O(n)이 소요한다. 그래서 deque 사용
      - deque 사용하면 인덱싱, 슬라이싱은 할수 없지만 데이터의 시작 혹은 끝에 데이터 삽입하는게 효과적이다.
      1. popleft() : 첫 원소 제거
      2. pop() : 마지막 원소 제거
      3. appendleft(x) : 첫 원소 삽입
      4. append(x): 마지막 원소 삽입
      - 그래서 파이썬에서 deque로 큐 자료구조로 이용할땐 선입선출이 될 수 있도록 append() 를 사용하고 popleft()를 사용하여 먼저 들어온 요소가 먼저 나가도록 구현한다.
   2. Counter

      - 와... 리스트와 같은 iterable 객체 내부 원소가 몇번 등장했는지 알려준다.
      - 와... js로 했을때 구현하기 어려웠던 건데 python은 바로 해주네

      ```python
      from collections import Counter

      counter = Counter(['red', 'blue', 'red','green','blue'])

      print(counter['blue'])
      print(dict(counter))
      #{'red': 2, 'blue': 2, 'green': 1}
      ```

6. math : 필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼 , 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수도 포함하고 있다
   1. factorial()
   2. math.sqrt()
   3. math.gcd() : 최대 공약수
