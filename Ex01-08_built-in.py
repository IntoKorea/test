# Ex01-08_built-in.py

# built-in 함수 (내장함수)

# round() : 소수점 값(실수값)에 대해 지정된 자릿수까지 반올림하는 함수
r = round(12.3456, 2)
print(f"r : {r}")
print()


# 크기 비교
# max() : 가장 큰 값을 구하는 함수
# min() : 가장 작은 값을 구하는 함수

data = [ 1, 7, 4, 5, 2 ]
print(f"data {data}")
print(f"큰 값   : {max(data)}")
print(f"작은 값 : {min(data)}")

# sum() : 모든 값에 대한 총합
tot = sum(data)
print(f"총합 : {tot}")


# pow() : 거듭 제곱을 구하는 함수
p = pow(4, 3)
print(f"pow(4, 3) : {p}")

# divmod() : 나눗셈 결과의 몫과 나머지를 구하는 함수
d1, d2 = divmod(4, 3)
print(f"4/3의 몫 : {d1}, 나머지 : {d2}")


# abs() : 절대값을 구하는 함수
d3 = -5
print(f"{d3} 절대값 : {abs(d3)}")


# chr() : 숫자를 문자로 변환하는 함수
# - 아스키코드값을 가지고, 해당 코드에 지정된 문자를 변환합니다.
value = 65
tv = chr(value)
print(f"value : {value}")
print(f"{value} chr={tv}") # 65를 아스키코드값의 문자로 변경. (65 -> A)

value = 48
tv = chr(value)
print(f"value : {value}")
print(f"{value} chr={tv}") # 48를 아스키코드값의 문자로 변경. (48 -> 0)


# ord() : 문자를 숫자로 변환하는 함수
value = 'A'
tv = ord(value)
print(f"value : {value}")
print(f"{value} ord={tv}")

value = '0'
tv = ord(value)
print(f"value : {value}")
print(f"{value} ord={tv}") 