from PIL import Image
import os

from pdf2image import convert_from_path

import pytesseract


def get_file_with_test():

    try:

        scanned_name = input("What is the name of your scanned file? Please include the file extension. ")
        if os.path.join(scanned_name):

            pdf_path = os.path.join(scanned_name)
            image = convert_from_path(pdf_path)

            save_name = input("What would you like to name your file? Do not type the file extension. ")

            for i in range(len(image)):
                image[i].save(save_name + '.png', 'PNG')

            save_txt = save_name + '.txt'

            output_file = os.path.join(save_name + '.png')

            with open(save_txt, "w") as file:
                file.write(pytesseract.image_to_string(Image.open(output_file)))
            
            os.remove(output_file)
    
    except:
        print("Sorry, that file was not found.")
        get_file_with_test()
    
    else:
        print("Output file generated.")
        attempt_to_print(save_txt)

def attempt_to_print(file):
    answer = input("Would you like to print the output file? (y/n): ")
    if answer == "y":
        os.startfile(file, "print")
    elif answer == "n":
        print("Thank you for using this program.")
    else:
        print("Sorry, incorrect input.")
        attempt_to_print(file)

get_file_with_test()