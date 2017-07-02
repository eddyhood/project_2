import logging

logging.basicConfig(filename = "cipherlogs.log", level=logging.INFO)


class Cipher:
    """Parent class that all uniques ciphers extend from. Takes a single
    string argument from the user as the text to be encrypted or
    decrypted."""
    def __init__(self, message, touch_pad = None, *args, **kwargs):
        self.message = message
        self.touch_pad = touch_pad
