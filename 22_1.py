# Sander Rubenkov and Anastasija Vikhrova
#1
a = 1000        # Ввожу переменную а которая равна 1000
while a<1300:   #Использую цикл while и ставлю условие а<1300
    print (a)   #Принтую переменную а
    a+=3        #Выполняется вычисление пока а<1300
#2
a=1             #Вводится переменная а, которая равна 1
while a<110:    #Использую цикл while и ставлю условие a<110
    print(a)    #Вывожу на экран а
    a+=2        #Выполняется вычисление пока a<110
#3
a=90            # Ввожу переменную
while a>0:      #Цикл while с условием 
    print(a)    #Выводится на экран вычисления происходящие с 
    a-=5         #c переменной
#4 
a=2              #Ввожу переменную а
while a<1048577: #Ввожу цикл а с условием 
    print(a)     #Вывожу на экран переменную с вычислениями
    a*=2
#5
i = 2           #То же самое
while i < 10000:#То же самое
    print(i)    #То же самое
    i=2 * i - 1 #То же самое
#6
a = -166                       #Ввожу переменную а, которая равна -166 
while a<100:                    #Ввожу цикл while с условием ...
    if - 100<a<-9 or 9<a<100:   # Ввожу оператор условия, и ввожу условие 
        print(a)                 #Вывожу на экран переменную а
    a=2*(a-1)+200                #Переменная а выводится на экран с вычислениями
#7                               #которые я ввёл

n=int(input('n='))                #вожу функцию инпут(даю возможность пользователю
i=1                               #ввести с клавиатуры число)
b=1                     
while i<=n:                          #Пока условие верно, выполняется цикл 
    b*=1                              #и выводится итог на экран
    i+=1
print(b)
#8         
n = int(input('n='))                 #Пользователь вводит чисто с клавы
b=0                                  # ввожу перемен.
i=1                                  # ввожу переменн
for i in range(1,999):               #Ввожу цикл фор и ставлю условие (в диапазоне от 1 до 999)
    if b==n%i:                       # Если условие верно, выполняется принтуется на экран переменная
        print(i)

    
#10
neChet = 3  #-ввожу переменную
chet = 2    #-ввожу переменную
 
i = 3      #ввожу переменную
 
while i <=20:    #Ввожу цикл while и ставлю услловтие
    if(i%2 != 0):          #Ввожу условие if и ставлю условие
        neChet= 2 * neChet - 2         #(условие)
        print(neChet)                #Если условие верно выводится переменная на экран с вычислениями
    else:                           #В обратном случае
        chet = 2 * chet -2              #вводятся вычисления которые будут производится, " в противном случае"
        print(chet)                         #принтуется переменная
    i = i + 1
#11
a = 1             #Ввожу переменную
b = 1             #Ввожу переменную
c = 0             #Ввожу переменную
print(a, " " , b)    #Вывожу на экран
i = 3        
while i < 11:           #Ввожу цикл
    c = a + b              #условие
    a = b         #uslovie
    b = c       #uslovie
    print(c)      #пока выполняется условие цикла , принтуется переменная с
    i = i + 1
#
n = int(input())         #Вводим любое число
sum = 0                 #переменная 0
while(n != 0):               #Вводим цикл с улосвием
    sum = sum + (n % 10)        #Условие цикла
    n = n //10                      
    print(sum)                 #Пока выполняется условие цикла принтуется переменная 












































