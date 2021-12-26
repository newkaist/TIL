# 파이썬 병아리반
# 파이썬 병아리반
1. 출력과 입력 그리고 변수
name = '탁형'
print(name+'님! 안녕하세요')


name = input()
print(name+'님! 안녕하세요!')

name = input('이름을 입력하세요 : ')
print(name+'님! 안녕하세요!')

age = input('나이를 입력해주세요! : ')
print(age-4)
 >>TypeError: unsupported operand type(s) for -: 'str' and 'int'
 # age로 입력된 input 값은 str이고 -4는 int 이므로 input을 int로 변환해야한다.
 
 age = input('나이를 입력해주세요! : ')
print(int(age)-4)

2. 연산자 사용하기

2-1 산술 연산자
* : 곱셈
** : 거듭제곱
% : 나머지
/ : 실수 나눗셈
// : 정수 나눗셈

2-2 비교 연산자 (comparsion operator)
A >= B : A는 B보다 크거나 같다.
A <= B : A는 B보다 작거나 같다.
A == B : A는 B와 같다.
A != B : A는 B와 같지 않다.

2-3 논리 연산자 (logical operator)
A and B : A 와 B 둘 다 만족하면 True   
A or  B : A 와 B 둘 중 하나라도 만족하면 True 
A not B : A 는 B가 아니다. # 값이 0 이라면 False

3. 함수 불러오기

import random
dice=random.randint(1,6)
print(dice)

import math
print(math.sqrt(2))
# 파이썬 공식문서
http://docs.python.org/ko/3/library/index.html

4. 반복과 선택

4-1 for 반복문

for 반복문의 구조:
 for A in B :         # 맨 뒤의 콜론 명심
     반복할 문장 1     # 들여쓰기(문단구분)가 되어 있음
     (반복할 문장n)    # 보통 공백 문자([space]) 4개를 사용함

# 예제
name = '이탁형'
for i in name : 
    print(i)

for i in range(100):
    print(i**2)
# range(2,100,3) >>> 2부터 100미만의 정수가 3의 간격으로 출력

4-2 if 조건문
 
 if 조건문의 구조:
  if 조건 : 
      조건이 참일 경우 실행할 문장1 
      (조건이 참이경우 실행할 문장1)

# 예제
 if 10>0:
     print('안녕하세요?')
     
     
 if 10 !=0 and 5%2==1 :
     print('안녕하세요?')

 passwd = int(input('비밀번호 4자리를 입력해주세요 : '))
 if = passwd == 1531:
     print('비밀번호가 일치합니다.')
else :
    print('다시 입력해 주세요')
    
5. 순서 있는 저장공간 리스트
names = ['쵸파','루피','조로','상디']

-slicing
name[0:2] == name[:2]

-append
names.append('나미') #리스트에 값을 추가
print(names)

-length 
len() : 리스트의 길이, 문자열의 길이 출력
 
# 예제

names = ['쵸파', '루피', '상디', '조로']
names.append('해적왕')
for name in names :
    if len(name) > 2 :
        print(name, '왔나요~?')
        