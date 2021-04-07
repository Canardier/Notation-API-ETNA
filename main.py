#!/usr/bin/env python
# coding: utf-8
import requests
from authentification import authentification
from api import *
from menu import *

SESSION = requests.Session()

def main():
    if authentification() == 1:
        # student = input("Entrer le login d'un student pour obtenir ces notes: ")
        # get_student_mark(student)
        menu()

if __name__ == "__main__":
    main()