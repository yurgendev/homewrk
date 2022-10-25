#homework 1
# 1 task:
print ('Hello world')

# 2 task
print ('msg1')
print ('random message')
print ('123 345')

# 3 task:
sideA = 10
sideB = 12

area = sideA * sideB

print("Area of rectangle is: ", area)

# 4 task:

num1 = 10
num2 = 25

sum = num1 + num2
print("Sum of num1 and num2 is: ", sum)

product = num1 * num2
print("Multiple of num1 and num2: ", product)

difference = num1 - num2
print("difference of our numbers is: ", difference)

quotient = num1 / num2
print("quotient of our numbers is: ", quotient)

# 5 task:

pi = 3.14159
r = 10                  # радиус
d = 2 * r               # диаметр
DO = 2 * pi * r         #длинна окружности
s = 2 * pi * r ** 2                       #площать круга


print ("Радиус", r)
print ("Диаметр", d)
print ("Длинна окружности", DO)
print ("Площадь круга", s)


# homework 2
#task 1

q1 = "123"
int(q1)
print(int(q1))

#task 2
float(int(q1))
print(float(int(q1)))

#task 3

w1 = 12.345
int(w1)

#task 4

card1 = 1234_4567_7634_2323

last4 = card1 / 10000


print(last4)
# OR
credit1 = '1234 4214 1521 5132'
code = credit1[-4:]
#OR
code2 = credit1[-4:].rjust(len(credit1), '*')

print(code)
print(code2)

#task 5

three = 123
answer = (three // 100) + (three // 10 % 10) + (three % 10)
print(answer)

#task 6
t1 = 3
t2 = 4
t3 = 5
p = (t1 + t2 + t3) / 2
newarea = p * (p - t1) * (p - t2) * (p - t3) ** 0.5
print(newarea)

# task 7

number_1 = int(input("Text first number: "))
number_2 = int(input("Text 2nd number: "))
number_3 = int(input("Text 3rd number: "))


print('Sum of our numbers is: ', number_1 + number_2 + number_3)

# task 8

we_need_their_count = 123123125134123123333
print(len(str(we_need_their_count)))

# task 9

numbers_for_revers_order = 123456789
print(str(numbers_for_revers_order)[::-1])










