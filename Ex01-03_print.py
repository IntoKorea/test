# Ex01-03_print.py

name = "son"
print("Hi", name)
print("Hi " + name) # 문자열은 결합이 가능합니다. (타입이 같은 문자열에서는 '+'(결합) 사용 가능. 문자와 숫자는 결합 x.)

age = 30
print("나이 :", age)
# print("나이 :" + age) # Error : 문자열과 숫자는 결합할 수 없습니다.

print()



'''
변수 포맷을 사용한 출력
- print("서식문자" % (데이터))
  > 출력 데이터와 서식문자의 개수, 순서, 타입은 일치해야 합니다.
%d : 정수
%f : 실수
%s : 문자열
%c : 문자
'''
print("숫자 : %d" % (10))
print("이름 : %s - 나이 : %d" % (name, age))

print()

#-------------------------------------------------------------------------------------------

'''
format() 함수
- print("{}".format())
- 출력 내용 안의 {}(포맷필드) 위치에 데이터를 출력할 수 있습니다.
- 변수의 타입을 지정하지 않아도 됩니다.
'''
print("숫자 : {}".format(10))
print("이름 : {} - 나이 : {}".format(name, age)) # 변수 포맷 쓰는 것 보다 가독성 좋음.

print()

#-------------------------------------------------------------------------------------------

'''
f-string
- print(f"{ }")
- 출력 내용 앞에 f 를 붙이고, {} 를 사용해서 변수를 추가합니다.

'''
print(f"숫자 : {10}")
print(f"이름 : {name} - 나이 : {age}") # 변수 포맷 쓰는 것 보다 가독성 좋음.

print()

#-------------------------------------------------------------------------------------------


'''
실수 출력시 소수점 자리 조정
- {:f}
'''
height = 123.456
print("높이 : {:.2f}".format(height)) # {:.2f} 소수점 둘째 자리까지 출력(반올림)
print(f"높이 : {height:.2f}") 

print()

#-------------------------------------------------------------------------------------------

'''
십진수 값 변환 출력
'''
value = 10
print("10진수 : {}".format(value))
print("2진수 : {:b}".format(value)) #{:b} 2진수
print("8진수 : {:o}".format(value)) #{:o} 
print("16진수 : {:x}".format(value)) #{:x}

print()

#-------------------------------------------------------------------------------------------

'''
출력 필드 폭 지정
- {:숫자}
- 숫자 만큼의 자리를 지정해서 출력
- < : 왼쪽 맞춤
  ^ : 가운데 맞춤
  > : 오른쪽 맞춤
  숫자는 기본이 오른쪽 맞춤이고, 문자열은 기본이 왼쪽 맞춤입니다.
'''
# 숫자는 자리를 의미함. < , ^, > 기호는 위치를 의미함.
# 숫자는 기본적으로 오른쪽 맞춤.
digitA = 123
print("{:5}|".format(digitA)) 
print("{:<5}|".format(digitA))
print("{:^5}|".format(digitA))
print("{:>5}|".format(digitA))
print()

# 문자열은 기본적으로 왼쪽 맞춤.
digitB = "abc"
print("{:5}|".format(digitB)) 
print("{:<5}|".format(digitB))
print("{:^5}|".format(digitB))
print("{:>5}|".format(digitB))
print()


#-------------------------------------------------------------------------------------------
