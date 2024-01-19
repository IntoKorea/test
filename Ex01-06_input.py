# Ex01-06_input.py

# input() 함수
# print("데이터 입력 > ", end="")
# data = input()
# print(f"data : {data}")
# print()

# # input() 함수의 () 안에 출력메시지를 지정해줄 수 있습니다.
data = input("문자열 입력 > ")
print(f"문자열 : {data}")
print()


# # input() 함수를 사용해서 입력한 모든 값은 모두 문자열로 처리됩니다.(input함수는 모든 데이터를 문자열로 처리함)
v1 = input("첫번째 입력 > ")
v2 = input("두번째 입력 > ")
print(f"{v1} + {v2} = {v1+v2}") # 문자열 이어서 출력됨
print(f"v1 type : {type(v1)}, v2 type : {type(v2)}") 
print()


# # 입력받은 데이터는 형변환을 이용해서 원하는 자료형으로 사용해야 합니다. 
d1 = input('정수 입력_1 > ')
d2 = input('정수 입력_2 > ')
d1 = int(d1)
d2 = int(d2)
print(f"{d1} + {d2} = {d1+d2}") # 숫자가 덧셈 처리됨

# 한줄로 여러개의 변수 선언 가능
d1, d2 = int(d1), int(d2)
print(f"{d1} + {d2} = {d1 + d2}")


no1 = 1
no2 = 2
d3 = int(input(f"숫자 입력_{no1} > "))
d4 = int(input(f"숫자 입력_{no2} > "))
total = d3 + d4
print(f"{d3} + {d4} = {total}")


# 한번에 여러개의 입력값을 처리할 때는 입력값을 공백으로 분할합니다.
d5, d6 = input("두개의 데이터를 입력하세요\n>> ").split() # 입력값 넘어가면 split으로 해당 값 분할(split은 문자열함수임)

print(f"입력값 : {d5}, {d6}")
