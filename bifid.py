import logging
from ciphers import Cipher
from helper_functions import divide_by_five, divide_by_two,remove_encryption_spaces

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)


class Bifid(Cipher):
    """Encodes a message by using two different lists of letters / characters and matching the index value of the "movable" list to that of the fixed"""

    encrpyted_message = []

    coordinates = {
                   "b":(1, 1), "g":(2, 1), "w":(3, 1), "k":(4, 1), "z":(5, 1),
                   "q":(1, 2), "p":(2, 2), "n":(3, 2), "d":(4, 2), "s":(5, 2),
                   "i":(1, 3), "o":(2, 3), "a":(3, 3), "x":(4, 3), "e":(5, 3),
                   "f":(1, 4), "c":(2, 4), "l":(3, 4), "u":(4, 4), "m":(5, 4),
                   "t":(1, 5), "h":(2, 5), "y":(3, 5), "v":(4, 5), "r":(5, 5)
    }

    @classmethod
    def create_bifid(cls, *args, **kwargs):
        """creates an instance of Alberti by getting message from user"""
        message = input("Enter a message to encrypt / decrypt: ")
        logging.info("User message created: {}".format(message))
        return cls(message)

    def get_coordinates(self):
        x_coordinates = []
        y_coordinates = []
        remove_spaces = remove_encryption_spaces(self.message)

        for letter in remove_spaces:
            position = self.coordinates[letter.lower()]
            x_coordinates.append(position[0])
            y_coordinates.append(position[1])
        logging.info("X coordinates are: {}".format(x_coordinates))
        logging.info("y coordinates are: {}".format(y_coordinates))

        final_coordinates = x_coordinates + y_coordinates
        logging.info("final coordinates are: {}".format(final_coordinates))
        return final_coordinates

    def encrypt(self):
        coordinates = self.get_coordinates()

        n = 2
        split = [coordinates[i:i+n] for i in range(0, len(coordinates), n)]
        logging.info("Split: {}".format(split))

        code_letters = []
        coordinate_tuples = self.coordinates.items()

        for data in split:
            for letter, coordinate in self.coordinates.items():
                if data == list(coordinate):
                    code_letters.append(letter)

        join_letters = "".join(code_letters)
        divide_message = divide_by_five(join_letters)
        logging.info("Code is: {}".format(divide_message))
        return divide_message







