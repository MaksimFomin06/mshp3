class Student:
    def __init__(self, name, surname, hp, sanity, excitement):
        self.name: str = name
        self.surname: str = surname
        self.hp: int = hp
        self.sanity: int = sanity
        self.excitement: int = excitement

    def start_game(self):
        self.name, self.surname = input().split()
        self.num = int(input())
        self.hp = 100
        self.sanity = 100
        self.excitement = 50
        self.iq = 20
        self.energy = 100
        for i in range(self.num):
            xod = input()
            if xod == "Wait":
                self.wait()
            elif xod == "Eat":
                self.eat()
            elif xod == "Study":
                self.study()
            elif xod == "Sleep":
                self.study()
            elif xod == "Watch TV":
                self.watch_tv()
            self.show()

    def is_alive(self):
        while self.hp > 0:
            return True
        return False
    
    def eat(self):
        if self.is_alive():
            self.hp += 1
            self.energy += 7
            self.iq -= 1
            self.excitement -= 2

    def wait(self):
        if self.is_alive():
            self.hp += 1
            self.energy -= 3
            self.excitement -= 3

    def study(self):
        if self.is_alive():
            self.hp -= 2
            self.energy -= 4
            self.iq += 5
            self.sanity -= 5
            self.excitement -= 2
    
    def sleep(self):
        if self.is_alive():
            self.hp += 2
            self.energy -= 2
            self.sanity += 7

    def watch_tv(self):
        if self.is_alive():
            self.hp -= 2
            self.energy -= 3
            self.iq -= 3
            self.sanity += 1
            self.excitement += 5

    def show(self):
        if self.is_alive():
            print(f"{self.name} {self.surname}: HP = {self.hp}, Energy = 0{self.hp}, IQ = 0{self.iq}, Sanity = {self.sanity}, Excitement = 0{self.excitement}.")    
        else:
            print(f"{self.name} {self.surname}: HP = {self.hp}. Game Over")
    

app = Student(1, 1, 1, 1, 1)
app.start_game()