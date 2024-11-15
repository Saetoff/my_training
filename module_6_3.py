import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения существа

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful:)")
        else:
            print("Be careful, i'm attacking you 0_0")




class Bird(Animal): # птицы
    beak = True # Наличие клюва

    def lay_eggs(self):
        eggs_count = random.randint(1,5)
        print(f"Here are(is) {eggs_count} eggs for you")



class AquaticAnimal(Animal):  # рыбы
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        change_in_z = abs(dz) * self.speed / 2
        self._cords[2] -= change_in_z



class PoisonousAnimal(Animal): # Ядовитые животные
    _DEGREE_OF_DANGER = 8



class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

if __name__ == '__main__':

    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()
