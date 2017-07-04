import logging
from pad import create_pad

logging.basicConfig(filename = "cipherlogs.log", level=logging.INFO)


class Cipher:
    """Parent class that all uniques ciphers extend from. Takes a single
    string argument from the user as the text to be encrypted or
    decrypted."""
    def __init__(self, message, one_time_pad = None, keyword = None, size = None, *args, **kwargs):
        for letter in message:
            if letter.isalpha() or letter == " " or letter is "&":
                pass
            else:
                logging.warning("User tired to enter a message with special charicters.")
                raise ValueError("Your message can only contain letters from the english alphabet.")
        self.message = message
        #Get one-time pad information for each cipher
        one_time_pad = input("Please enter the one-time pad number: ")
        keyword = input("Enter a keyword that is shorter than your pad: ")
        size = input("Encryption in blocks of 5? Y/n")
        self.one_time_pad = one_time_pad
        self.keyword = keyword
        self.size = size
        create_pad(self.one_time_pad, self.keyword)
        logging.info("Message:  {}, One_Time_Pad: {}, Keyword: {} Size {}".format(self.message, self.one_time_pad, self.keyword, self.size))
