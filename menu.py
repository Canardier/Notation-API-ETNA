import __main__ as main
from api import *

def fun1():
    print("function 1")
    get_student_mark(get_env("LOGIN"))

def fun2():
    print("function 2")
    get_student_mark(input("login du student en question: "))

def fun3():
    get_note(get_promo_bach2023())

def effect(choice):
    choice = int(choice) - 1
    my_function = (
        fun1,
        fun2,
        fun3
    )
    my_function[choice]()


def menu():
    file = open("./asset/menu.txt", "r")
    choice = input(file.read())
    effect(choice)
