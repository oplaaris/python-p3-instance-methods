#!/usr/bin/env python3
from lib.dog import Dog


class Person:
    # Class body goes here
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
    # Instance method definition
    my_dog = Dog("Buddy")
    # Call the bark method
    my_dog.bark()
    # Call the sit method
    my_dog.sit()
