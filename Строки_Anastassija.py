#1
s="masha1234"
print(s[2])     #1
print(s[4])     #2
print(s[0:5])   #3
print(s[0:4])   #4
print(s[::2])   #5
print(s[1::2])  #6
print(s[::-1])  #7
print(s[::-2])  #8
print(len(s))   #9
#2
print(input().count(" ") + 1)
#3
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
#4
s = input()
fff = s[:s.find(' ')]
sss = s[s.find(' ') + 1:]
print(sss + ' ' + fff)
#5
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
#6
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
#7
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#8
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#9
print(input().replace('1', 'one'))
#10
print(input().replace('@', ''))
#11
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
#12
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)