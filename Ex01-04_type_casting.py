# Ex01-04_type_casting.py

'''
자료형( data type )
- 데이터를 보관하는 공간의 형식을 정의합니다.
- type()
  > 변수에 저장되어 있는 데이터의 자료형을 확인하는 함수입니다.
'''

'''
bool 자료형
- True, False값을 가질 수 있습니다. (파이썬은 맨 앞글자가 대문자)
'''
b1 = True
b2 = False
print(f"b2 : {b2} - 자료형 : {type(b2)}")
print()

'''
int ( 정수 )
'''
i1 = 10
i2 = -11
print(f"i2: {i2} - 자료형 : {type(i2)}")
print()


'''
float ( 실수 )
'''
f1 = 1.2
print(f"f1: {f1} - 자료형 : {type(f1)}")
print()


'''
str ( 문자열 )
'''
s1 = "문자열"
print(f"s1 : {s1} - 자료형 : {type(s1)}")
print()


'''
tuple ( 튜플 )
- 소괄호
'''
tu_1 = ( 1, 2, 3 )
print(f"tu_1 : {tu_1}")
print(f"자료형 : {type(tu_1)}")
print()

'''
list ( 리스트 )
- 대괄호
'''
list_1 = [ 'a', 'b', 'c' ]
print(f"list_1 : {list_1}")
print(f"자료형 : {type(list_1)}")
print()

'''
set ( 세트 )
- 중괄호
'''
set_1 = { 1, 2, 3 }
print(f"set_1 : {set_1}")
print(f"자료형 : {type(set_1)}")
print()

'''
dict ( 딕트 )
- 중괄호(키 : 벨류)
'''
dict_1 = {"k1":"v1", 'k2':'v2'} # java의 map 역할임.
print(f"dict_1 : {dict_1}")
print(f"자료형 : {type(dict_1)}")
print()

print()

#-------------------------------------------------------------------------------------------

'''
자료형 변환
'''

# bool() : 부울형으로 변환
print("- bool() -")
print(bool(0), bool(1), bool(-1)) # False True True (0:False, 0 제외한 나머지: True)
print(bool(0.0), bool(1.2), bool(-2.3)) # False True True 
print(bool(''), bool('b'), bool(' ')) # False True True (비어있는 경우:False, 값 있으면 :True / 공백도 값이 있는 것임.)
print(bool([]), bool([1, 2])) # False True (비어있는 경우:False, 값 있으면 :True)

value1 = 1
cast1 = bool(value1)
print(f"cast1 : {cast1} - type {type(cast1)}")
print()


# str() : 문자열로 변환
print("- str() -")
print(str(123), str(-123), str(1.2))

value2 = 123
# print('value2' + value2) # Error. 문자열과 숫자는 '+'로 결합 안됨.
value2 = str(value2)
print('value2 : ' + value2) 


# int() : 정수형으로 변환
print("- int() -")
print(int(True), int(False)) # True:1, False:0
print(int('123'), int('-123'))
print(int(1.2), int(-2.3)) # 실수는 소수점 잘림
# print(int('a')) # Error : 숫자형태의 문자열만 int 타입으로 형변환이 가능합니다.
print()

# float() : 실수형으로 변환
print("- float() -")
print(float(True), float(False)) # True:1.0, False:0.0
print(float('123'), float('-123'))
print(float(1.2), float(-2.3)) # 실수는 소수점 잘림
# print(float('a')) # Error : 숫자형태의 문자열만 float 타입으로 형변환이 가능합니다.
print()


# tuple 변환
print("- tuple() -")
tu_2 = tuple("abcde")
print(f"tu_2 {tu_2}") # 결과: tu_2 ('a', 'b', 'c', 'd', 'e')
print()

# list 변환
print("- list() -")
list_2 = list("abcde")
print(f"list_2 {list_2}") # 결과: list_2 ['a', 'b', 'c', 'd', 'e']
print()

# dict 변환
print("- dict() -")
# dict_2 = dict("abcde") # Error (dictionary update sequence element)
dict_2 = dict([('k1', 'value1'), ('k2', 'value2')]) # 한개의 set()을? list?로 감싸면 가능함.
print(f"dict_2 {dict_2}") # 결과: dict_2 {'k1': 'value1', 'k2': 'value2'}
print()


print()
