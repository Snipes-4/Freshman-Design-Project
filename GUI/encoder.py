
class Encoder:

    def __init__(self, message: str, key: str):
        self.message = [x for x in message]
        self.original_message = message
        self.message_indexes = {}
        self.key = [x for x in key]
        self.key_indexes = {}
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        for x in self.message:
            indexes = [i for i in range(len(self.message)) if self.message[i] == x]
            self.message_indexes.update({str(x): indexes})

        for letter,key in zip(self.alphabet,self.key):
            self.key_indexes.update({str(letter): str(key)})

    def encode(self):
        for x in self.original_message:
            replace = self.key_indexes.get(str(x))
            for index in self.message_indexes[x]:
                self.message.pop(index)
                self.message.insert(index, replace)

    def __str__(self):
        result = ''.join(self.message)
        return result

    
            

    
