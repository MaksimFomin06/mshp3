class Student:
    def __init__(self, name, surname, hp):
        self.name = name
        self.surname = surname
        self.hp = hp

    def start_game(self):
        self.name, self.surname = input().split()
        self.hp = 100

    def is_alive(self):
        while self.hp > 0:
            return True
        return False
    def show(self):
        if self.is_alive():
            print(f"{self.name} {self.surname}: HP = {self.hp}.")
        else:
            print(f"{self.name} {self.surname}: HP = {self.hp}. Game Over")

app = Student(1, 1, 1)
app.start_game()
app.show()