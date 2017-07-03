import logging
from ciphers import Cipher
from helper_functions import divide_by_five, remove_encryption_spaces

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)


class Key(Cipher):
    """uses a keyword to shift alphabetic text and pair the letters for encryption"""

    encrpyted_message = []

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, message, keyword, *args, **kwargs):
        super(). __init__(message, touch_pad = None, *args, **kwargs)
        self.keyword = keyword


    @classmethod
    def create_keyword(cls, *args, **kwargs):
        """creates an instance of the keyword cipher by getting a message and a keyword from the user"""
        message = input("Enter a message to encrypt / decrypt: ")
        keyword = input("Enter a word with no duplicate letters as a keyword. For example, 'Kryptos' would work but 'Bob' would not: ")

        for letter in keyword:
            if keyword.count(letter) > 1:
                raise ValueError("You chose a keyword with duplicate letters.  Please try again. For example, 'Kryptos' would work but 'Bob' would not.")
            else:
                logging.info("User message created: {}".format(message))
                return cls(message, keyword)

    def encrypted_alphabet(self, keyword):
        encrypted_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for letter in keyword:
            if letter in encrypted_alphabet:
                encrypted_alphabet.remove(letter)

        encrypted_alphabet = [letter for letter in keyword] + encrypted_alphabet

        logging.info("Encrypted alphabet: {}".format(encrypted_alphabet))
        return encrypted_alphabet

    def encrypt(self):
        get_encrypted_alphabet = self.encrypted_alphabet(self.keyword)
        remove_spaces = remove_encryption_spaces(self.message)

        for letter in remove_spaces:
            get_index = self.alphabet.index(letter.lower())
            get_code = get_encrypted_alphabet[get_index]
            self.encrpyted_message.append(get_code)

        logging.info("Encrypted message is: {}".format(self.encrpyted_message))
        return self.encrpyted_message








