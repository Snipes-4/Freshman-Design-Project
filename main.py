from decoder import Decoder

decode_this = input("Enter the message to decode: ")
d1 = Decoder(decode_this)
running = True
while (running == True):
    print("")
    print(d1)
    print(d1.original_message)
    print("")
    command = input("What would you like to do? ")
    match command:
        case "undo":
            letter = input("What would you like to undo? ")
            d1.undo(letter)
            print("Done!")
        case "replace":
            letter = input("What would you like to replace? ")
            new_letter = input("And what do you want to replace it with? ")
            d1.replace_letter(letter, new_letter)
            print("Done!")
        case "frequency":
            d1.frequency()
            print(d1.letter_frequency)
            print("Done!")
        case "exit":
            running = False
        case _:
            print("Invalid input, try again")


