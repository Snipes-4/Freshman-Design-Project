
class Decoder:

    def __init__(self, message: str):
        self.message = [x for x in message]
        self.original_message = message
        self.letter_frequency = {}
        self.message_indexes = {}

        for x in self.message:
            indexes = [i for i in range(len(self.message)) if self.message[i] == x]
            self.message_indexes.update({str(x): indexes})
        
    def frequency(self):
        for x in self.message:
            count = self.message.count(str(x))
            percent = int(float(count/len(self.message)) * 100)
            self.letter_frequency.update({str(x): str(percent)})

    def replace_letter(self, chosen_letter, new_letter):
        if chosen_letter in self.original_message:
            for index in self.message_indexes[chosen_letter]:
                self.message.pop(index)
                self.message.insert(index, new_letter)
        else:
            print("Error: Letter not in message. Please try again.")

    def undo(self, chosen_letter):
        if chosen_letter in self.original_message:
            for index in self.message_indexes[chosen_letter]:
                self.message.pop(index)
                self.message.insert(index, chosen_letter)
        else:
            print("Error: Letter not in message. Please try again.")
                
    def __str__(self):
        result = ''.join(self.message)
        return result


    


    