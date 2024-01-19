# Ex01-03_Quiz.py

'''
Q1) 이름, 나이, 키를 변수에 저장해서 출력하세요
- 키는 소수점 첫째자리까지만 출력합니다.
'''

name="손흥민"
age=30
height=175.36

# 방법1
print(f"이름 : {name}")
print(f"나이 : {age}세")
print(f"키 : {height:.1f}")

# 방법2
# print("이름 :", name)
# print("나이 : {}세".format(age))
# print(f"키 : {height:.1f}")

print()

#-------------------------------------------------------------------------------------------

'''
Q2) 오늘 날짜(년 월 일)의 숫자만 변수로해서 출력합니다.
'''
# 방법1
from datetime import datetime
today = datetime.today().strftime("%Y%m%d")
print(today)

# 방법2
year = 2024
month = 1
day = 16
print(f"{year}년 {month}월 {day}일")

print()

#-------------------------------------------------------------------------------------------