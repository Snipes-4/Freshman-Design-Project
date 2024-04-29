from decoder import Decoder
from encoder import Encoder

what_to_do = input("What are we doing? ")
if what_to_do == "decode":
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
            case "key":
                key = input("What key do you want to use? ")
                d1.generate_key(key)
                d1.decode_by_key()
                print("Done!")
            case "exit":
                running = False
            case _:
                print("Invalid input, try again")
elif what_to_do == "encode":
    #word: fortnite
    #key : soqtrkjdnpgbufimalevcyzxhw
    encode_this = input("Enter the message to encode: ")
    encode_key = input("Enter key in lowercase and alphabetical order: ")
    e1 = Encoder(encode_this, encode_key)
    print("")
    print(e1)
    print("")

    e1.encode()

    print(e1)
    print("")
else:
    print("What")


