import sys
import os

from alberti import Alberti
from keyword_cipher import Key
from bifid import Bifid


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def call_encrypt(choice):
    if choice == 1:
        message = Alberti.create_alberti()
        encryption = Alberti.encrypt(message)
        print("Your encrypted message is {}".format(encryption))

    elif choice == 2:
        message = Key.create_keyword()
        encryption = Key.encrypt(message)
        print("Your encrypted message is {}".format(encryption))

    elif choice == 3:
        message = Bifid.create_bifid()
        encryption = Bifid.encrypt(message)
        print("Your encrypted message is {}".format(encryption))


def call_decrypt(choice):
    if choice == 1:
        message = Alberti.create_alberti()
        decryption = Alberti.decrypt(message)
        print("Your decrypted message is {}".format(decryption))

    elif choice == 2:
        message = Key.create_keyword()
        decryption = Key.decrypt(message)
        print("Your decrypted message is {}".format(decryption))

    elif choice == 3:
        message = Bifid.create_bifid()
        decryption = Bifid.decrypt(message)
        print("Your decrypted message is {}".format(decryption))


def display_ciphers():
    print("Available cipher methods are:\n#1 - Alberti Cipher\n#2 - Keyword Cipher\n#3 - Bifid Cipher")


def launch_menu():
    goal = input("Welcome to Hood's Cipher System. Would you like to encrypt, decrypt, or quit?  Choose E / D / Q:")

    if goal.upper() == "E":
        clear_screen()
        display_ciphers()
        choice = input("Type number 1 - 9 to choose your cipher method: ")
        call_encrypt(int(choice))

    elif goal.upper() == "D":
        clear_screen()
        display_ciphers()
        choice = input("Type number 1 - 9 to choose your cipher method: ")
        call_decrypt(int(choice))

    elif goal.upper() == "Q":
        clear_screen()
        print("Thanks for using Hood's Cipher System")
        sys.exit()

    else:
        raise ValueError("Please enter E, D, or Q")

go = launch_menu()
