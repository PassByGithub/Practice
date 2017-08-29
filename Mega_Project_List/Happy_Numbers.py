from math import sqrt

def ishappy(x):
    flag=0
    digits = []
    memory=[]
    while x!=1:
        #把数字分割开存储到list里面
        while x:
            digits.append(x % 10)
            x //= 10
        x=sum(list(map(lambda x:x**2,digits)))
        if x in memory:
            break
        else:memory.append(x)
        if x==1:
            flag=1
            break
        digits = []
    if flag==1:
        return True
    else:return False

while True:
    print('')
    number = input("Up to which number do you want")
    try:
        number=int(number)
        for i in range(1, number):
            if ishappy(i):
                print(i,end=' ')
    except ValueError:  #输入的不是数字
        if number=='quit':
            break
        print("you enter an wrong number")
print("done!")



# numbers_found = 1
# happy_numbers = [1]
# i = 2
# while numbers_found != 8:
#     j = i
#     string_number = str(i)
#     sum_of_squares = 0
#     memory = []
#     memory.append(i)
#     while True:
#         for k in string_number:
#             sum_of_squares += int(k) ** 2
#         if sum_of_squares in memory:
#             break
#         if sum_of_squares == 1:
#             happy_numbers.append(i)
#             numbers_found += 1
#             break
#         memory.append(sum_of_squares)
#         string_number = str(sum_of_squares)
#         sum_of_squares = 0
#     i += 1
#
# print (happy_numbers)

#
# def get_digits(number):
# 	digits = []
# 	while number:
# 		digits.append(number % 10)
# 		number //= 10
# 	digits.reverse()
# 	return digits
#
# def is_happy_number(number):
# 	previous_numbers = []
# 	while True:
# 		digits = get_digits(number)
# 		sum_of_squared_digits = sum(list(map(lambda x: x **2, digits)))
# 		if sum_of_squared_digits == 1:
# 			return True
# 		elif sum_of_squared_digits in previous_numbers:
# 			return False
# 		else:
# 			number = sum_of_squared_digits
# 			previous_numbers.append(number)
#
# def print_happy_number(number):
# 	happy_numbers = []
# 	count = 0
# 	while count < 8:
# 		if is_happy_number(number):
# 			happy_numbers.append(number)
# 			count += 1
# 		number += 1
# 	return happy_numbers
#
# print(print_happy_number(int(input())))