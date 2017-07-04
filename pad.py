import logging

logging.basicConfig(filename = "cipherlogs.log", level=logging.INFO)


def create_pad(one_time_pad, keyword):
    """Takes the users entered pin and keyword to create a new cipher text
    that secures their message even further."""
    alphabet = {
                "a":1, "b":2, "c":3, "d":4, "e":5,
                "f":6, "g":7, "h":8, "i":9, "j":10,
                "k":11, "l":12, "m":13, "n":14, "o":15,
                "p":16, "q":17, "r":18, "s":19, "t":20,
                "u":21, "v":22, "w":23, "x":24, "y":25, "z":26
                }

    #get the cooresponding #'s for each letter in user's keyword
    get_nums = []
    for letter in keyword:
        for character, position in alphabet.items():
            if letter == character:
                get_nums.append(position)
    logging.info("Nums for keyword are:  {}".format(get_nums))

    #combine both number lists and add
    keyword_length = len(keyword)
    match_pad = str(one_time_pad[:keyword_length+1])
    pad_list = [int(num) for num in match_pad]
    combine = list(zip(pad_list, get_nums))
    added = [num1 + num2 for num1, num2 in combine]

    #Covered added totals into letters for encryption
    get_encrypted_letters = []
    for num in added:
        for character, position in alphabet.items():
            if int(num) == position:
                get_encrypted_letters.append(character)
    final_encryption = "".join(get_encrypted_letters)
    logging.info("Final encryption is {}".format(final_encryption))
    return final_encryption
