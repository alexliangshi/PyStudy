# -*- coding:utf-8 -*-

class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor Called ")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


# bill_cyrus = Parent("shiliang", "brown")
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.eye_color)
print(miley_cyrus.number_of_toys)
