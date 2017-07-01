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
    """Encodes a message by getting a user generated key and using it to combine both the real_letters and encoded_letters lists for a cipher
    """

    message_formatted = []
    message_with_digraph = []
    encrpyted_message = []

    real_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n",
                            "o", "p", "q", "r", "s", "t", "v", "x", "z",
                            1, 2, 3, 4]

    encoded_letters = ["D", "L", "G", "A", "Z", "E", "N", "B", "O", "S",
                       "F","C", "H", "T", "Y", "Q", "I", "X", "K", "V",
                       "P", "&","M", "R"]

    digraph = {"H":"FF",
               "J":"II",
               "K":"QQ",
               "U":"VV",
               "W":"XX",
               "Y":"ZZ"
               }

    secret_marker = "K"

    def __init__(self, message, letter_key, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.letter_key = letter_key

        #Check for letter in possible options
        if letter_key in ["H", "J", "K", "U", "W", "Y"]:
            logging.warning("User entered something other than a letter.")
            raise ValueError("That letter will not work.  Remember that H, J, K, U, W, and Y are not options for a key")

        logging.info("User message: {}, user key: {}".format(self.message, letter_key))

    @classmethod
    def create_alberti(cls, *args, **kwargs):
        #creates an instance of Alberti by getting message & key from user
        message = input("Enter a message to encrypt / decrypt: ")
        letter_key = input("Enter a single letter as a key.  Note that H, J, K, U, W, and Y are not options for a key: ").upper()
        return cls(message, letter_key)

    def format_alberti(self):
        #Before you can encrypt, each word should start with a caps to make the cipher stronger.
        cap_word = self.message.title()
        for letter in cap_word:
            if letter == " ":
                continue
            else:
                self.message_formatted.append(letter)
        logging.info("by letter is {}".format(self.message_formatted))

    def add_digraphs(self):
        #The cipher requires that certain letters be replaced with digraphs before the message can be encoded.

        for letter in self.message_formatted:
            if letter.upper() in self.digraph:
                self.message_with_digraph.append(self.digraph[letter.upper()])
            else:
                self.message_with_digraph.append(letter)

        logging.info("With digraph is {}".format(self.message_with_digraph))

    def encrypt(self):

        #complete encryption
        start_index = self.real_letters.index(self.letter_key.lower())
        logging.info('Starting point is {}'.format(start_index))
        pass




    def decrypt(self):
        pass
