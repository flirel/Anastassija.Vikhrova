#1
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
#2
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
#3
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
#4
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
#5
x = int(input())
p = int(input())
y = int(input())
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print(i)
#6
len = 0
while int(input()) != 0:
    len += 1
print(len)
#7
sum = 0
element = int(input())
while element != 0:
    sum += element
    element = int(input())
print(sum)
#8
sum = 0
len = 0
element = int(input())
while element != 0:
    sum += element
    len += 1
    element = int(input())
print(sum / len)
#9
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)
#10
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1       
print(num_maximal)

