letters = list("abcdefghijklmnopqrstuvwxyz")
message = input("Enter a message: ").lower()


def shift_number(shift = False):
    while not shift:

        try:
            shift = int(input("Enter a shift number: "))

        except ValueError:
            print("Enter a Number!")

    return shift


def shift_letters(shift):
    new_message = ""

    for char in message:

        if char in letters:
            index = letters.index(char) - shift
            new_message += letters[index]

        else:
            new_message += char 

    return new_message


shift = shift_number()
message = shift_letters(shift)
print(message)
