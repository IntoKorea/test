# Ex01-07_operator.py

# 산술연산자
data1, data2 = 4, 3
print(f"{data1} ** {data2} = {data1**data2}") # 거듭제곱 : **
print(f"{data1} // {data2} = {data1//data2}") # 나눗셈 결과의 몫을 구하는 연산자 : //


# not : 참 또는 거짓에 대한 부정
not True
not False
print(f"not {data1} > {data2} : {not data1>data2}") # not: 결과의 부정


# 멤버 연산자
# n in () : () 안의 데이터 중에 n의 값이 있는지 확인
# n not in () : () 안의 데이터 중에 n의 값이 없는지 확인
print(f"{data1} in (1, 2, 3, 4, 5) : {data1 in (1, 2, 3, 4, 5)}")
print(f"{data1} not in (1, 2, 3, 4, 5) : {data1 not in (1, 2, 3, 4, 5)}")


# 식별 연산자
# type() is 자료형
print(f'type({data1}) is int : {type(data1) is int}')
print(f'type({data1}) is float : {type(data1) is float}')


# 논리연산자 (and, or) (기호 아님주의)
# and : 모든 값이 참인 경우에 참
# or  : 모든 값이 거짓이면 거짓 (하나라도 참이면 참)
a = True
b = False
print(a and b)
print(a or b)