import os
import logging

logging.basicConfig(filename = "cipherlogs.log", level=logging.INFO)


class Cipher:
    """Parent class that all uniques ciphers extend from. Takes a single
    string argument from the user as the text to be encrypted or
    decrypted."""
    def __init__(self, message, *args, **kwargs):
        self.message = message


class Alberti(Cipher):
    """Compares & combines two lists of letters to encode the message.
    Each time a capital letter is found in the message, the two lists
    are zipped together so that (x = Capital letter, Y = encoded message.)

    The original cipher did not contain all letters of the alphabet so
    some unique attributes are assigned to deal with that.
    """

    def __init__(self, message, letter_key, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.letter_key = letter_key

        real_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n",
                        "o", "p", "q", "r", "s", "t", "v", "x", "z",
                        1, 2, 3, 4]

        encoded_letters = ["D", "L", "G", "A", "Z", "E", "N", "B", "O", "S",
                           "F","C", "H", "T", "Y", "Q", "I", "X", "K", "V",
                           "P", "&","M", "R"]

        special_characters = {
                            "H":"FF",
                            "J":"II",
                            "K":"QQ",
                            "U":"VV",
                            "W":"XX",
                            "Y":"ZZ"
                            }

        #Check for letter in possible options
        if not letter_key in encoded_letters:
            logging.warning("User entered something other than a letter.")
            raise ValueError("That letter is not an option.  Please choose from the list.")

        logging.info("User message: {}, user key: {}".format(self.message, letter_key))

    @classmethod
    def create_alberti(cls, *args, **kwargs):
        message = input("Enter a message to encrypt / decrypt: ")
        letter_key = input("Enter a single letter as a key: ").upper()
        return cls(message, letter_key)

    def format_message(self):
        #Formats message to remove spaces between words to and add title caps
        cap_word = self.message.title()
        by_letter = []
        for letter in cap_word:
            if letter == " ":
                continue
            else:
                by_letter.append(letter)

        logging.info("by letter is {}".format(by_letter))
        return by_letter

    def encrypt_alberti(self):
        pass


    def decrypt_alberti(self):
        pass
