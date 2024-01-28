letters = list("abcdefghijklmnopqrstuvwxyz")
message = input("Enter a message: ").lower()
shift = False


while not shift:
    try:
        shift = int(input("Enter a shift number: "))
    except ValueError:
        print("Enter a Number!")


new_message = ""
for char in message:
    if char in letters:
        index = letters.index(char) - shift
        new_message += letters[index]
    else:
        new_message += char 


print(new_message)
