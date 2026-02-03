class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("woof")


class Cat(Animal):
    def make_sound(self):
        print("meow")


def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        animal.make_sound()


main()
