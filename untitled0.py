#1
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)
#2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
#3
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
#4
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)
#5
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
#6
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)
#7
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)
#8
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
#9
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)
#10
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
#11
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)