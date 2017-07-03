
def divide_by_five(final_message):

    #remove random spacing from message
    formatted_message = []
    for letter in final_message:
        if letter == " ":
            continue
        else:
            formatted_message.append(letter)

    #Split list into lists with 5 chararcters each
    n = 5
    split = [formatted_message[i:i+n] for i in range(0, len(formatted_message), n)]

    #Combine letters within each of the lists
    combine = ["".join(data) for data in split]

    #combine the groups of combined lists
    joined_list = []
    for data in combine:
        space = data + " "
        joined_list.extend(space)

    #covert final list to string
    final_encryption = "".join(joined_list)

    return final_encryption

def remove_encryption_spaces(message):
    without_spaces = []
    for letter in message:
        if letter == " ":
            continue
        else:
            without_spaces.append(letter)
    return without_spaces


