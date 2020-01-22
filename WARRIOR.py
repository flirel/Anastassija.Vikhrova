import random #Модуль random для генерации случайных чисел
class Warrior():
    """Класс Воин."""
    hp = 100 #переменная для здоровья
    dmg = 20 #переменная для урона
    """метод, возвращающий кол-во дамага война"""
    def damage(self):
        return self.dmg
    def defence(self,a):
        """метод, берущий число, вычитающий его из хп.""" 
        """Оператор if"""
        self.hp-=a
        if self.hp<=0:
            return False
        else:
            return True

a = 2 # кол-во юнитов
warriors = [Warrior() for i in range(0,a)]#генерация войнов
Game = True # переменная, при котором игра начнётся
"""Цикл While для самой игры"""
while Game: # выход если условие неверное (Game = True)
    # выбор атакующего и защитника
    attacker = random.randint(0,a-1)
    defender = random.randint(0,a-1)
    # юнит не может атаковать сам себя
    while attacker == defender:
        defender = random.randint(0,a-1)
    """Битва"""
    #если кто-то умирает значение переменной Game меняется, игра завершается
    Game = warriors[defender].defence(warriors[attacker].damage())
    print(attacker,'юнит атаковал, у юнита ',defender,'осталось',warriors[defender].hp,'единиц здоровья')
"""Победитель"""
print('Юнит',attacker,'- красавчик, который','унизил и закидал помидорами юнита',defender)