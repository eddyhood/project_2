import logging
from ciphers import Cipher
from helper_functions import divide_by_five, remove_encryption_spaces

logging.basicConfig(filename="cipherlogs.log", level=logging.INFO)


class Bifid(Cipher):
    """Encodes a message by assigning each letter in the user's message to an (x,y) coordinate system and then scrambling the values."""

    encrpyted_message = []

    coordinates = {
                   "b":(1, 1), "g":(1, 2), "w":(1, 3), "k":(1, 4), "z":(1, 5),
                   "q":(2, 1), "p":(2, 2), "n":(2, 3), "d":(2, 4), "s":(2, 5),
                   "i":(3, 1), "o":(3, 2), "a":(3, 3), "x":(3, 4), "e":(3, 5),
                   "f":(4, 1), "c":(4, 2), "l":(4, 3), "u":(4, 4), "m":(4, 5),
                   "t":(5, 1), "h":(5, 2), "y":(5, 3), "v":(5, 4), "r":(5, 5)
    }

    @classmethod
    def create_bifid(cls, *args, **kwargs):
        """creates an instance of Bifid by getting message from user"""
        message = input("Enter a message to encrypt / decrypt: ")
        logging.info("User message created: {}".format(message))
        return cls(message)

    def get_coordinates(self):
        """Takes each letter from  the user's message and assigns an (x, y" coordinate for each one."""
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

    def get_coordinates_decrypt(self):
        """Takes each letter from  the secret message and assigns an (x, y" coordinate for each one."""
        code_coordinates = []
        remove_spaces = remove_encryption_spaces(self.message)

        for code in remove_spaces:
            for letter, coordinates in self.coordinates.items():
                if code.lower() == letter:
                    code_coordinates.append(coordinates)

        return code_coordinates

    def encrypt(self):
        """Encrypts the users message"""
        coordinates = self.get_coordinates()
        join = [data for data in coordinates]
        logging.info("joined for decryption is: {}".format(join))

        n = 2
        split = [coordinates[i:i+n] for i in range(0, len(coordinates), n)]
        logging.info("Split: {}".format(split))

        code_letters = []

        for data in split:
            for letter, coordinate in self.coordinates.items():
                if data == list(coordinate):
                    code_letters.append(letter)

        join_letters = "".join(code_letters)
        divide_message = divide_by_five(join_letters)
        logging.info("Code is: {}".format(divide_message))
        return divide_message

    def decrypt(self):
        """Decrypts the user's secret message"""
        coordinates = self.get_coordinates_decrypt()
        logging.info("Get coordinates for decrypt:  {}".format(coordinates))
        length = (len(coordinates) / 2)
        x_coordinates = coordinates[:int(length)]
        y_coordinates = coordinates[int(length):]

        x_list = []
        for data in x_coordinates:
            convert = list(data)
            x_list.extend(convert)
        logging.info("x_list: {}".format(x_list))

        y_list = []
        for data in y_coordinates:
            convert = list(data)
            y_list.extend(convert)
        logging.info("y_list: {}".format(y_list))

        zipped_coordinates = list(zip(x_list, y_list))
        logging.info("zipped coordinates: {}".format(zipped_coordinates))

        decrypted_message = []
        for position in zipped_coordinates:
            for letter, coordinates in self.coordinates.items():
                if position == coordinates:
                    decrypted_message.append(letter)

        join_letters = "".join(decrypted_message)


        logging.info("Decrypted message is:  {}".format(join_letters))
        return join_letters



