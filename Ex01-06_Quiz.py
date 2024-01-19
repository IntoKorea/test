# Ex01-06_Quiz.py

'''
Q1)
이름을 입력하세요 > xxx
xxx님의 나이를 입력하세요 > 20
xxx님의 전화번호를 입력하세요 > 010-1234-5678
'''

# print("이름을 입력하세요 > ", end="")
# name = input()
# print(f"{name}님의 나이를 입력하세요 > ", end="")
# age = input()
# print(f"{name}님의 전화번호를 입력하세요 > ", end="")
# phoneNum = input()

# print(f"{name}님 | {age}세 | 전화번호 : {phoneNum}")

# print()

#-----------------------------------------------------------------------------------


'''
Q2)
태어난 년도를 입력받아서 나이를 계산하세요

'''
# print("태어난 년도 입력 >> ", end="")
# year = input()
# year = int(year)
# print(f"나이 : {2024 - year + 1}")

# #모범답안
# currentYear = 2024
# year = int(input("태어난 년도 입력 > "))
# age = currentYear - year + 1
# print(f"나이 : {age}")

#-----------------------------------------------------------------------------------


'''
Q3)
키를 입력받아서, 해당 키의 표준 체중을 구하세요
- 표준 체중 = ( 키 - 100 ) X 0.9
- 결과는 소수점 첫째 자리까지만 나오게 합니다.
'''

print("키 >> ", end="")
height = input()
height = float(height)
nomal = (height - 100)*0.9
print(f"표준 체중 : {nomal:.1f}")

#방법2
# nomal = round((height - 100)*0.9, 1)
# print(f"표준 체중 : {nomal}")

#-----------------------------------------------------------------------------------

# 모범답안
height = float(input('키 입력 > '))
weight = (height - 100)*0.9
print(f"키 : {height}의 표준 체중 : {weight:.1f}kg")