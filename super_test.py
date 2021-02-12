class Dog:
    def __init__(self):
        print("woof woof")


class Puppy(Dog):
    def __init__(self):
        super().__init__()
        print("I'm tiny")


p = Puppy()