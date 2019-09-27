## algorithm_study based on [this book](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9788931459500&orderClick=LAG&Kc=), [this lecture](https://www.udemy.com/course/python-programming-algorithms-data-structures/) and problems based on [this site](https://www.acmicpc.net/)

<br>

## Python Tips

### 1. 몫, 나머지 구하기

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

### 2. 진법 변환하기

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

### 3. 문자열 정렬하기

보통 다음과 같이 문자열을 정렬하고자 할 때,
~~~
'가나다라               ' # 좌측정렬
'               가나다라' # 우측 정렬
'       가나다라        ' # 가운데 정렬
~~~

다른 언어에서는 (혹은 이 기능을 모르는 사람은)
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

### 4. 알파벳 출력
다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통 'abcdefg ....'와 같이 손수 알파벳을 입력하곤 합니다. 

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

