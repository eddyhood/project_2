import sys
import os
from alberti import Alberti
from keyword_cipher import Key
from bifid import Bifid
from helper_functions import clear_screen


def use_again():
    choice = input("\nWould you like do use Hood's Cipher System again?  Y/n")
    if choice.upper() == "Y":
        launch_menu()
    else:
        clear_screen()
        print("Thanks for using Hood's Cipher System")
        sys.exit()


def call_encrypt(choice):
    """Depending on the cipher the user picks, this function calls the class method for that cipher (creating an instance) and then calls the encrypt method for it."""
    if choice == 1:
        message = Alberti.create_alberti()
        encryption = Alberti.encrypt(message)
        print("Your encrypted message is {}".format(encryption))
        use_again()

    elif choice == 2:
        message = Key.create_keyword()
        encryption = Key.encrypt(message)
        print("Your encrypted message is {}".format(encryption))
        use_again()

    elif choice == 3:
        message = Bifid.create_bifid()
        encryption = Bifid.encrypt(message)
        print("Your encrypted message is {}".format(encryption))
        use_again()


def call_decrypt(choice):
    """Depending on the cipyer the user picks, this function calls the class method for that cipher (creating an instance) and then calls the decrypt method for it."""
    if choice == 1:
        message = Alberti.create_alberti()
        decryption = Alberti.decrypt(message)
        print("Your decrypted message is {}".format(decryption))
        use_again()

    elif choice == 2:
        message = Key.create_keyword()
        decryption = Key.decrypt(message)
        print("Your decrypted message is {}".format(decryption))
        use_again()

    elif choice == 3:
        message = Bifid.create_bifid()
        decryption = Bifid.decrypt(message)
        print("Your decrypted message is {}".format(decryption))
        use_again()


def display_ciphers():
    """Shows the user which ciphers are available for use."""
    print("Available cipher methods are:\n\n#1 - Alberti Cipher\n#2 - Keyword Cipher\n#3 - Bifid Cipher\n")


def launch_menu():
    """Launches the program and introduces the user to Hood's Cipher System.  It gives them the ability to choose a cypher, a method, and learn about each cipher."""
    clear_screen()
    print("=================TOP SECRET CLEARANCE REQUIRED=================\n")

    goal = input("Welcome to Hood's Cipher System!\nWould you like to encrypt, decrypt, or quit?\n\n**You can also type HELP to learn about the ciphers. Choose E / D / Q / HELP: ")

    if goal.upper() == "E":
        clear_screen()
        display_ciphers()
        choice = int(input("Type number 1, 2, or 3 to pick a cipher for encryption: "))
        if choice >= 1 and choice <=3:
            call_encrypt(choice)
        else:
            raise ValueError("Please type 1, 2, or 3.")

    elif goal.upper() == "D":
        clear_screen()
        display_ciphers()
        choice = int(input("Type number 1, 2, or 3 to pick a cipher for decryption: "))
        if choice >= 1 and choice <=3:
            call_decrypt(choice)
        else:
            raise ValueError("Please type 1, 2, or 3.")

    elif goal.upper() == "Q":
        clear_screen()
        print("Thanks for using Hood's Cipher System")
        sys.exit()

    elif goal.upper() == "HELP":
        print("====================The Alberti Cipher====================\n")
        print("The Alberti Cipher Disk described by Leon Battista Alberti in his treatise De Cifris embodies the first example of polyalphabetic substitution with mixed alphabets and variable period.\nThis device, called Formula, is made up of two concentric disks, attached by a common pin, which can rotate one with respect to the other.\nThe larger one is called Stabilis [stationary or fixed], the smaller one is called Mobilis [movable]. The circumference of each disk is divided into 24 equal cells.\nThe outer ring contains one uppercase alphabet for plaintext and the inner ring has a lowercase mixed alphabet for ciphertext. The outer ring also includes the numbers 1 to 4 for the superencipherment of a codebook containing 336 phrases with assigned numerical values.\nThis is a very effective method of concealing the code-numbers, since their equivalents cannot be distinguished from the other garbled letters. The sliding of the alphabets is controlled by key letters included in the body of the cryptogram.\n\n")
        print("====================The Keyword Cipher====================\n")
        print("A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.\nRepeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A,B,C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.\n\n")
        print("====================The Bifid Cipher====================\n")
        print("In classical cryptography, the bifid cipher is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion. It was invented around 1901 by Felix Delastelle.\nLonger messages are first broken up into blocks of fixed length, called the period. The period is 5 so solve for 5 letters at a time. Each block is then encrypted separately. Statistical analysis to detect the period uses ciphertext letters. Since each letter corresponds to two numbers, it infers half the period, not the period directly. Thus, odd periods are more secure than even, because the statistical anomalies register both on half the period rounded down and rounded up.\n\n")

        start_again = input("Want to get started? Y/n")
        if start_again.upper() == "Y":
            launch_menu()
        else:
            clear_screen()
            print("Thanks for using Hood's Cipher System\n")
            sys.exit()

    else:
        raise ValueError("Please enter E, D, Q, or HELP")

go = launch_menu()
