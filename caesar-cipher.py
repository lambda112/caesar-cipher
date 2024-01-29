from art import logo


def type_shift():
    shift_type = input("Type encode to encrypt, type decode to decrypt: ").lower()

    while shift_type not in ("encode", "decode"):
        print("Enter valid shift type!\n")
        shift_type = input("Type encode to encrypt, type decode to decrypt: ").lower()

    return shift_type



def shift_number(shift = False, shift_type = "encode"):

    while not shift:
        try:
            shift = int(input("Enter a shift number: "))
        except ValueError:
            print("Enter a Number!\n")

    if shift_type == "encode":
        return shift
    else:
        return -shift



def shift_letters(shift, letters = list("abcdefghijklmnopqrstuvwxyz")):

    message = input("Enter a message: ").lower()
    new_message = ""

    for char in message:

        if char in letters:
            index = letters.index(char) - shift
            index = index % 26
            new_message += letters[index]

        else:
            new_message += char 

    return new_message



def end_program():

    finished = input("Finished, type yes or no: ")

    while finished not in ("yes", "no"):
        print("Type yes or no\n")
        finished = input("Finished, type yes or no: ")
    
    return finished



def main():

    finished = False
    while finished != "yes":

        shift_type = type_shift() 
        shift = shift_number(False, shift_type)
        message = shift_letters(shift)
        print(f"Output: {message}")

        finished = end_program()
        print(" ")
    

print(logo)
main()

    