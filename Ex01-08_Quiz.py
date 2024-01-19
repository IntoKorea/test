# Ex01-08_Quiz.py

#Q1) 2, 5, 15, 3, 7 의 총합, 평균을 구하세요.
data = [2, 5, 15, 3, 7]
total = sum(data)
avg = total / 5
print(total)
print(avg)

#-----------------------------------------------------------------------------------

#Q2) 2, 5, 15, 3, 7 의 큰값에 대한 작은값의 거듭제곱을 구하세요.
maxNum = max(data)
minNum = min(data)
print(f"큰값에 대한 작은값의 거듭제곱 : {maxNum**minNum}")

# 방법2
print(f"큰값에 대한 작은값의 거듭제곱 : {pow(maxNum, minNum)}")
