import logging
import random
from ciphers import Cipher
from helper_functions import divide_by_five, remove_encryption_spaces

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)


class Alberti(Cipher):
    """Encodes a message by using two different lists of letters / characters and matching the index value of the "movable" list to that of the fixed"""

    encrpyted_message = []

    fixed = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n",
                            "o", "p", "q", "r", "s", "t", "v", "x", "z",
                            1, 2, 3, 4]

    movable = ["d", "l", "g", "a", "z", "e", "n", "b", "o", "s",
                       "f", "c", "h", "t", "y", "q", "i", "x", "k", "v",
                       "p", "&", "m", "r"]

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
        """creates an instance of Alberti by getting message from user"""
        message = input("Enter a message to encrypt / decrypt: ")
        logging.info("User message created: {}".format(message))
        return cls(message)

    def spin(self):
        """Spins movable "wheel" in relation to fixed wheel for encryption"""
        pointer_index = self.movable.index(self.pointer)
        letter_shift = random.choice(self.fixed[:20])
        shift_index = self.fixed.index(letter_shift)
        diff_index = pointer_index - shift_index
        spin = self.movable[diff_index:] + self.movable[:diff_index]
        add_key_letter = self.encrpyted_message.append(letter_shift.upper())
        logging.info("pointer index: {}, letter shift: {}, shift index: {}, diff index: {}, spin: {}".format(pointer_index, letter_shift, shift_index, diff_index, spin))
        return spin

    def decrypt_spin(self, letter):
        """Spins movable "wheel" in relation to fixed wheel for decryption"""
        pointer_index = self.movable.index(self.pointer)
        code = letter.lower()
        code_index = self.fixed.index(code)
        diff_index = pointer_index - code_index
        spin = self.movable[diff_index:] + self.movable[:diff_index]
        logging.info("Decrypted spin pointer index: {}, code: {},  code index: {}, diff_index{} spin{}".format(pointer_index, code, code_index,diff_index, spin))
        return spin

    def add_digraphs(self):
        """The cipher requires that certain letters be replaced with digraphs before the message can be encoded. This makes the message harder to crack."""
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
        """Encrypts the message from user"""
        add_digraphs = self.add_digraphs()
        start_spin = self.spin()

        for letter in add_digraphs:
            if len(self.encrpyted_message) != 0 and len(self.encrpyted_message) % self.shift_range == 0:
                start_spin = self.spin()
                get_letter_index = self.fixed.index(letter)
                get_coded_letter = start_spin[get_letter_index]
                space = self.encrpyted_message.append(" ")
                encrypt = self.encrpyted_message.append(get_coded_letter)
            else:
                get_letter_index = self.fixed.index(letter)
                get_coded_letter = start_spin[get_letter_index]
                encrypt = self.encrpyted_message.append(get_coded_letter)

        if self.size.upper() == "Y":
             final_encryption = divide_by_five(self.encrpyted_message)
             logging.info("Encrypted Msg is: {}".format(final_encryption))
             return final_encryption
        else:
            logging.info("Encrypted Msg is: {}".format("".join(self.encrpyted_message)))
            return "".join(self.encrpyted_message)

    def decrypt(self):
        """Decrypts the message from user"""
        start_spin = []
        message_with_digraphs = []
        remove_spaces = remove_encryption_spaces(self.message)
        logging.info("Remove spaces for decryption = {}".format(remove_spaces))

        for letter in remove_spaces:
            if letter.istitle():
                start_spin = self.decrypt_spin(letter)
            else:
                get_letter_index = start_spin.index(letter)
                get_coded_letter = self.fixed[get_letter_index]
                message_with_digraphs.append(get_coded_letter)

        join_list = "".join(message_with_digraphs)
        logging.info("Message with digraphs: {}".format(join_list))

        double_digraphs = {
                            "h":"ff",
                            "j":"ii",
                            "k":"qq",
                            "u":"vv",
                            "w":"xx",
                            "y":"zz"
                        }

        digraphs = double_digraphs.items()

        for letter, code in digraphs:
            if code in join_list:
                join_list = join_list.replace(code, letter)

        logging.info("Message without digraphs: {}".format(join_list))
        return join_list
