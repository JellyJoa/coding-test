# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
a = int(input())
b = int(input())
print(a // b)


# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
f1 = float(input())
f2 = float(input())
print(f1 ** f2)


# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
a, b = input().split()
print(int(a) ** int(b))

# 단어와 반복 횟수를 입력받아 여러 번 출력해보자
a, b = input().split()
print(a*int(b))
c = input()
d = int(input())
print(c*d)


# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1*f2)


# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
a = ord(input())
print(chr(a+1))


# 입력된 정수의 부호를 바꿔 출력해보자.
a = int(input())
print(-a)


# 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
n = int(input())
n = chr(n)
print(n)


# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
a = ord(input())
print(a)


# 16진수를 입력받아 8진수(octal)로 출력해보자.
n = int(input(),16)
print('%o' % n)


# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
a = int(input())
print('%x' % a)
print('%X' % a)


# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(a + b)


# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
h,m,s = input().split(':')
print(m)
a = input().split(':')
print(a[1])


# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
date = input()
print(date[0:2])
print(date[2:4])
print(date[4:])


# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
a = input()
for i in a:
    print(i)


# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX
# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

a,b = input().split('-')
print(a+b)


# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y,m,d = input().split('.')
print(d,m,y, sep='-')


# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
a, b = input().split(':')
print(a, b, sep=":")


# 이번에는 특수문자 출력에 도전하자!!
#
# 다음 문장을 출력하시오.
#
# "!@#$%^&*()'

print('"!@#$%^&*()\'')


# 윈도우 운영체제의 파일 경로를 출력하는 연습을 해보자.
# 다음 경로를 출력하시오.

# "C:\Download\'hello'.py"

print('"C:\\Download\\\'hello\'.py"')


# 이번에는 다음과 같은 python프로그램의 소스코드를 출력해보자.
# print("Hello\nWorld")

print('print("Hello\\nWorld")')