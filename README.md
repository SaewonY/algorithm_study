## algorithm_study based on [this book](http://www.kyobobook.`c`o.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9788931459500&orderClick=LAG&Kc=), [this lecture](https://www.udemy.com/course/python-programming-algorithms-data-structures/) and problems based on [this site](https://www.acmicpc.net/)

<br>
<br>

## Summary
* [몫, 나머지 구하기](#몫,-나머지-구하기)
* [진법 변환하기](#진법-변환하기)


<br>
<br>

## 몫, 나머지 구하기

<br>

~~~
a = 7
b = 5
print(a//b, a%b)
~~~
위와 같이 보통 계산하지만 파이썬에서는 편리한 함수가 있다.

~~~
a = 7
b = 5
print(*divmod(a, b))
~~~
다만 수간 작을 경우 전자가 속도가 더 빠르다.

<br>

## 진법 변환하기

<br>

~~~
num = '3212'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
~~~
보통 위와 같이 for문을 돌며 계산하지만

~~~
num = '3212'
base = 5
answer = int(num, base)
~~~
파이썬은 진법 변환 내장함수를 지원한다. 참고로 int의 base 디폴트 값은 10이다.

<br>

## 문자열 정렬하기

<br>

보통 다음과 같이 문자열을 정렬하고자 할 때,
~~~
'가나다라               ' # 좌측정렬
'               가나다라' # 우측 정렬
'       가나다라        ' # 가운데 정렬
~~~

다른 언어에서는..

보통 for문을 돌며 공백문자를 여러 번 붙이지만,
~~~
### 우측 정렬 예
s = 'abc'
n = 7

answer = ''
for i in range(n-len('가나다라')): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += '가나다라'
~~~
파이썬에서는 ljust, center, rjust와 같은 method를 지원한다.

~~~
s = 'abc'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
~~~

<br>

## 알파벳 출력

<br>

다른 언어에서는..

보통 'abcdefg ....'와 같이 손수 알파벳을 입력하곤 한다. 

~~~
answer = 'abcdefghijk (편의상 생략)'
~~~
파이썬에서는 이런 데이터를 상수(contants)로 정의해 놓았다.
~~~
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
~~~

<br>

## 2차원 리스트 뒤집기

<br>

다른 언어에서는..

보통은 다음과 같이 2중 for문을 이용해 리스트의 row와 column을 뒤집는다.
~~~
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )
~~~
파이썬에는 zip과 unpacking을 이용하면 코드 한 줄로 뒤집을 수 있다.
~~~
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
~~~


- zip 함수 사용 예시1
~~~
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )
~~~
- zip 함수 사용 예시2
~~~
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
~~~

<br>

## 모든 멤버의 type 변환하기 - map

<br>

다른 언어에서는..

보통 사람들은 for 문을 이용해 원소의 타입을 하나씩 바꾼다.
~~~
list1 = ['1', '100', '33']
list2 = []
for i in list1:
    list2.append(int(i))
~~~
파이썬의 map을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있다.
~~~
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
~~~

<br>

## Sequence 멤버를 하나로 이어붙이기 - join

<br>

다른 언어에서는..

보통 사람들은 for 문을 이용해 원소를 하나씩 이어 붙인다.
~~~
my_list = ['1', '100', '33']
answer = ''
for i in list1:
    answer += i
~~~
파이썬에서는 join을 사용하면 간단하다.
~~~
my_list = ['1', '100', '33']
answer = ''.join(my_list)
~~~

<br>

## sequence type의 * 연산

<br>

다른 언어에서는..

보통 사람들은 for 문을 이용해 기존 스트링에 'abc'를 여러 번 붙이는 번거로운 일을 한다.
~~~
answer = ''
n = 어쩌고
for i in range(n):
    answer += 'abc'
~~~
파이썬에서는 *연산자를 사용해 코드를 획기적으로 줄일 수 있다.
~~~
n = 어쩌고
answer = 'abc'*n
~~~
또, * 연산자를 이용하면 [123, 456, 123, 456, 123 ...] 과같이 123, 456이 n번 반복되는 리스트를 만들 수 있습니다.
~~~
n = 어쩌고
answer= [123, 456]*n
~~~

<br>

## 곱집합, 혹은 조합 구하기

<br>

다른 언어에서는..

보통 사람들은 for 문을 이용해 두 iterable의 원소를 하나씩 곱해간다.

~~~
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for i in iterable1:
    for j in iterable2:
        for k in iterable3:
            print(i+j+k)
~~~
파이썬에서는 itertools.product를 이용하면, 

for 문을 사용하지 않고도 곱집합을 구할 수 있다.

~~~
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
~~~

- NOTE - 하나의 리스트 안에서 조합을 계산한다면 permutation, combination 사용

<br>

## 2차원 1차원 리스트로 만들기

<br>

다른 언어에서는..

보통 사람들은 반복문을 이용해 리스트를 더해간다.
~~~
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for i in my_list:
    answer += i
~~~
파이썬의 다양한 기능을 사용하면, for 문을 사용하지 않고도 리스트를 이어붙일 수 있다.
~~~
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
~~~

<br>

## 가장 많이 등장하는 알파벳 찾기

<br>

다른 언어에서는..

보통 사람들은 반복문을 이용해 수를 센다.
~~~
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
~~~
파이썬의 collections.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있다.
~~~
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
~~~

<br>

## for문과 if문을 한번에

<br>

다른 언어에서는..

보통 사람들은 for 문 안에서 조건문을 사용해 2-depth 블록을 만든다.
~~~
mylist = [3, 2, 6, 7]
answer = []
for i in mylist:
    if i%2 == 0:
        answer.append(i**2)
~~~
파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있다.
~~~
mylist = [3, 2, 6, 7]
answer = [ i**2 for i in mylist if i %2 == 0]
~~~

<br>

## 이진탐색하기 - binary search

<br>

다른 언어에서는..

직접 반복문을 만들어, 이진 탐색 알고리즘을 구현한다.
~~~
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
~~~
파이썬의 bisect.bisect 메소드를 사용하면 이 코드를 간략하게 만들 수 있다.
~~~
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
~~~

<br>

## 클래스 인스턴스 출력하기 - class의 자동 string casting

<br>

다른 언어에서는..

보통 사람들은 클래스 바깥에 출력 함수를 만들거나, print 문 안에서 format을 지정합니다.

~~~
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)
~~~

파이썬에서는 __str__ 메소드를 사용해 class 내부에서 출력 format을 지정할 수 있습니다
~~~
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
~~~

<br>

## 큰 수를 할당해야 할 경우 - inf

<br>

코테를 풀다 보면 아주 큰 값을 할당해야 하는 경우가 있다.
~~~
min_val = float('inf')
min_val > 10000000000
~~~
파이썬이 제공하는 inf를 사용하면 그 어떤 숫자와 비교해도 무조건 크다고 판정된다.
- NOTE: inf에는 음수를 붙이는 것도 가능하다.
~~~
max_val = float('-inf')
~~~

<br>

## 파일 입출력 간단하게

<br>

다른 언어에서는..

EOF를 만날 때까지, 파일 읽기를 반복합니다.

~~~
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    raw = line.split()
    print(raw)
f.close()
~~~
파이썬의 with - as 구문을 이용하면 코드를 더 간결하게 짤 수 있다.
~~~
with open('myfile.txt') as file:
  for line in file.readlines():
    print(line.strip().split('\t'))
~~~


<br>
<br>

## Python 복잡도

<br>

![LIST](https://user-images.githubusercontent.com/40786348/66254570-fb6e1000-e7b2-11e9-9619-aed89f044c05.png)

<br>

![1234](https://user-images.githubusercontent.com/40786348/66254612-bf877a80-e7b3-11e9-9c7f-20e79c3a5981.PNG)

- reference: https://wayhome25.github.io/python/2017/06/14/time-complexity/
