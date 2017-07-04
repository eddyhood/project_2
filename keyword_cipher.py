import logging
from ciphers import Cipher
from helper_functions import divide_by_five, remove_encryption_spaces

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)


class Key(Cipher):
    """Uses a keyword to shift alphabetic text and pair the letters for encryption"""

    encrpyted_message = []

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, message, keyword, *args, **kwargs):
        super().__init__(message, touch_pad = None, *args, **kwargs)
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
        """Takes their keyword, removes it's letters from the alphabet and then appends keyword with what is left of the alphabet"""
        encrypted_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for letter in keyword:
            if letter in encrypted_alphabet:
                encrypted_alphabet.remove(letter)

        encrypted_alphabet = [letter for letter in keyword] + encrypted_alphabet

        logging.info("Encrypted alphabet: {}".format(encrypted_alphabet))
        return encrypted_alphabet

    def encrypt(self):
        """Encrypts message by matching index values from the encrypted alphabet to a standard alphabet"""
        get_encrypted_alphabet = self.encrypted_alphabet(self.keyword)
        remove_spaces = remove_encryption_spaces(self.message)

        for letter in remove_spaces:
            get_index = self.alphabet.index(letter.lower())
            get_code = get_encrypted_alphabet[get_index]
            self.encrpyted_message.append(get_code)

        join_message = "".join(self.encrpyted_message)
        divide_message = divide_by_five(join_message)

        logging.info("Encrypted message is: {}".format(divide_message))
        return divide_message

    def decrypt(self):
        """decrypts a message by matching index values from the encrypted alphabet to a standard alphabet"""
        get_encrypted_alphabet = self.encrypted_alphabet(self.keyword)
        logging.info("Decrypt alphabet = {}".format(get_encrypted_alphabet))
        remove_spaces = remove_encryption_spaces(self.message)
        logging.info("Message without spaces: {}".format(remove_spaces))

        decrypted_message = []

        for letter in remove_spaces:
            get_index = get_encrypted_alphabet.index(letter)
            get_letter = self.alphabet[get_index]
            decrypted_message.append(get_letter)

        join_message = "".join(decrypted_message)

        logging.info("Decrypted message is: {}".format(join_message))
        return join_message








