import json
test = True
class Message:
    def __init__(self, receiver:str, sender:str, message:str = ""):
        self.__sender = sender
        self.__receiver = receiver
        self.__message = message
    def get_receiver(self):
        self.__receiver = receiver
    def get_sender(self, sender):
        self.__sender = sender
    def get_message(self):
        self.__message = message
    def save_message(self,receiver, sender, message):
        with open("social.json", "a") as file:
            json_obj = json.dump(a_dict, json.load(f))
class Message_manager:
    def __init__(self,sender:str,receiver:str):
        self.__sender = sender
        self.__receiver = receiver
if test:
    t = Interaction("John", "Mary")
    temp_dict = {}
    a_dict = {"From": "John", "To": "Mary", "Message": "Hello, Mary!"}
    with open("social.json", "a") as file:
        json_obj = json.dump(a_dict, json.load(f))
        
        
class