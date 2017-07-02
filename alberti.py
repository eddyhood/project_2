import logging
import random
from ciphers import Cipher

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)

class Alberti(Cipher):
    """Encodes a message by using two different lists of letters / characters and matching the index value of the "movable" list to that of the fixed"""

    encrpyted_message = []

    fixed = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n",
                            "o", "p", "q", "r", "s", "t", "v", "x", "z",
                            1, 2, 3, 4]

    movable = ["d", "l", "g", "a", "z", "e", "n", "b", "o", "s",
                       "f","c", "h", "t", "y", "q", "i", "x", "k", "v",
                       "p", "&","m", "r"]

    digraph = {"h":"f",
               "j":"i",
               "k":"q",
               "u":"v",
               "w":"x",
               "y":"z"
               }

    pointer = "k"
    shift_range = 5

    @classmethod
    def create_alberti(cls, *args, **kwargs):
        #creates an instance of Alberti by getting message from user
        message = input("Enter a message to encrypt / decrypt: ")
        logging.info("User message created: {}".format(message))
        return cls(message)

    def spin(self):
        pointer_index = self.movable.index(self.pointer)
        letter_shift = random.choice(self.fixed[:20])
        shift_index = self.fixed.index(letter_shift)
        diff_index = pointer_index - shift_index
        spin = self.movable[diff_index:] + self.movable[:diff_index]
        add_key_letter = self.encrpyted_message.append(letter_shift.upper())

        logging.info("pointer index: {0}, letter shift: {1}, shift index: {2}, diff index: {3}, spin: {4}".format(pointer_index, letter_shift, shift_index, diff_index, spin))
        return spin

    def add_digraphs(self):
    #The cipher requires that certain letters be replaced with digraphs before the message can be encoded.
        lower_case = self.message.lower()
        message_with_digraphs = []

        for letter in lower_case:
            if letter == " ":
                continue
            elif letter in self.digraph:
                message_with_digraphs.append(self.digraph[letter])
                message_with_digraphs.append(self.digraph[letter])
            else:
                message_with_digraphs.append(letter)

        logging.info("With digraph is {}".format(message_with_digraphs))
        return message_with_digraphs

    def encrypt(self):
        add_digraphs = self.add_digraphs()
        start_spin = self.spin()
        total_spins = len(self.message) // self.shift_range
        spin_count = 1

        for letter in add_digraphs:
                get_letter_index = self.fixed.index(letter)
                get_coded_letter = start_spin[get_letter_index]
                encrypt = self.encrpyted_message.append(get_coded_letter)
        # spin_again = self.spin()
        # spin_count += 1


        logging.info("Encrypted Message is: {} and total spins = {}".format(self.encrpyted_message, total_spins))





