#1
print("ПЕРВОЕ ЗАДАНИЕ!")
print(" ")
class Dog (object) :
    def __init__(self, age, name, weight) :
        self.age = age
        self.name = name
        self. weight = weight
dog = Dog("10", "Juliet", "15")
print(dog.name + " is sitting")
#2
print(" ")
print("ВТОРОЕ ЗАДАНИЕ")
print(" ")
class Person(object) :
    def __init__(self, name, cellphone, email) :
        self.name = name
        self.cellphone = cellphone
        self.email = email
person = Person("Nastja", "53363729", "anastassija.vikhrova@ivkhk.ee")
print(person.name + " Звонит Маме") 
print("Его новый телефон " + person.cellphone)
print("второй объект: ")
class Gamer(object) :
    def __init__(self, name, cellphone, email) :
        self.name = name
        self.cellphone = cellphone
        self.email = email
gamer = Gamer("Alexey", "58528256", "psina.dog@ivkhk.ee")
print(gamer.name + " Любит играть") 
print("Его новый емаил " + gamer.email)
#3
print(" ")
print("ТРЕТЬЕ ЗАДАНИЕ")
print(" ")
class myBird (object) :
    def __init__(self, bird, color, name, breed) :
        self.bird = bird
        self.color = color
        self.name = name
        self.breed = breed 
myBird = myBird("Ласточка", "Розовая", "Sunny", "Sun Conure")
print(myBird.bird  + "купила себе конфетку")
print("Она обычно " + myBird.color)
print(myBird.name + " Всего лишь 5 лет")
#4
print("")
print("ЧЕТВЕРТОЕ ЗАДАНИЕ")
class User (object) :
    def __init__(self, name, force, X, Y) :
        self.name = name 
        self.force = force
        self.X = X
        self.Y = Y
user = User("Vitja","35","180","90")
print("\nИмя Персонажа : " + user.name)
print("\nСила Персонажа : " + user.force)
print("\nКоординаты:")
print("\nX : " + user.X)
print("\nY : " + user.Y)
#5
print("")
print("ПЯТОЕ ЗАДАНИЕ")
class Pirson (object) :
    def __init__(self, name, money, nanci):
        self.name = name
        self.money = money
        self.nanci = nanci
pirson = Pirson("Nancy","100","человек")
print("\nЭто - " + pirson.name)
print("\nОна имеет " + pirson.money + " Долларов")
print("\nОна " + pirson.nanci)
#6 and 7 исправленный код
class Person:
    name = ""
    money = 0
bob = Person()
name = "Nastja"
money = 25
print (bob.name + "has", money, "dollars.")