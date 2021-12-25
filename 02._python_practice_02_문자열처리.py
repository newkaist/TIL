# 함수와 메소드
# 함수 : 함수(대상)
# 메서드 : 대상.매서드

# 대소 치환
v1='abcde' #문자(string)
v1.upper() #대문자 치환
'ABCDE'.lower() #소문자 치환
'ac def'.title() # camel 표기법(단어의 첫글자만 대글자로 치환)

#색인(문자열 추출)
'abcd'[0]
'abcd'[-2]
'abcd'[0:3]

#ex) '031)345-0834'에서 지역번호만 추출
vtel='031)345-0834'
vtel[0:3]

#문자열의 시작, 끝 여부 확인
# v1.startswith(prefix, # 시작 값 확인 문자
#               start,  # 확인할 시작 위치
#               end)    # 확인할 끝 위치

v1.startswith('b')
v1.startswith('b',1)
v1[1:].startswith('b')

# #v1.endswith(suffix,
#              start,
#              end)
v1
v1.endswith('e')
v1.endswith('E')

# 앞 뒤 공백 또는 문자 제거
'abc'=='abc'

' abc '.strip() #양쪽의 공백을 제거함
'abc'.strip('a')#문자제거시 사용
'abaca'.strip('a')#양쪽 끝 문자만 제거가능(중간 글자 삭제 불가)

' abcd'.lstrip()#leftstrip-왼쪽 공백제거
' abcd '.rstrip()#rightstrip-오른쪽 공백제거

#치환
# 'abcabc'.replace(old, #찾을 문자열
                 # new) #바꿀 문자열
                 
'abcabc'.replace('a','A')
'abcabc'.replace('ab','AB')
'abcabc'.replace('ab','')

# 문자열 분리
v1.split(sep) #분리 구분기호
'a/b/c/d'.split('/')
'a/b/c/d'.split('/')[1]

# 위치값 리턴
# 'abcd'.find(sub,   # 위치값을 찾을 대상(substitute:대신하는 사람, 대리자,대체물)
#             start, # 찾을 위치(시작점)
#             end)   # 찾을 위치(끝점)

v1
v1.find('b')

# ex. 전화번호에서 지역번호 추출 ')' 위치를 확인해서 그 이전까지 추출할 것

vtel
vnum=vtel.find(')')
vtel[0:vnum] # = vtel[:vum]

# 포함 횟수
'abcabcabc'.count('a') # 해당 인자가 포함된 횟수를 표기

# 형(type) 확인
type(v1)        # 데이터 타입 확인
v1.isalpha()    #문자 확인
v1.isnumeric()  # 숫자 확인 - 자주 사용

# 대소문자 확인
v1.isupper()   
v1.islower()   

# 문자열 결함
'a'+'b'

# 문자열 길이
len(v1) #length:길이
3/len(v1)

# 연습 문제
vname='tak'
vemail='tak@naver.com'
jumin='900405-1111111'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1]== 'm'
vname[1]== 'r'

# 2. vemail에서 이메일 아이디만 추출
base=vemail.find('@')
vemail[:base]

# 3. 주민번호에서 여자인지 확인 (참고 1:남자, 2:여자)
jumin[7]=='2'
jumin.split('-')[1][0]==2
# 900405<0,1111111<1,>>>1<0
list(jumin.split('-'))
#Out[75]: ['900405', '1111111']













