class Human:
    def __init__(self, age, height, weight) -> None:
        self.age = age
        self.height = height
        self.weight = weight

    def my_age(self):
        print(f"I'm {self.age} years old")

    def my_height(self):
        print(f"I'm {self.height} cm")


def main():
    nick = Human(28, 178, 70)
    nick.my_age()


main()
