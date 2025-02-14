import json

class Message:
    def __init__(self, sender:str, receiver:str, message:str = ""):
        self.__visited = False
        self.__sender = sender
        self.__receiver = receiver
        self.__message = message

    def get_receiver(self):
        return self.__receiver

    def get_sender(self):
        return self.__sender

    def get_message(self):
        return self.__message

    def get_visited(self):
        return self.__visited

    def set_visited(self, visited: bool):
        self.__visited = visited

class Message_manager:
    def __init__(self):
        self.__messages = []

    def add_message(self, sender, receiver, text):
        self.__messages.append(Message(sender, receiver, text))

    def get_sender_messages(self, sender):
        return [message for message in self.__messages if message.get_sender() == sender]

    def get_receiver_messages(self, receiver):
        return [message for message in self.__messages if message.get_receiver() == receiver]

    def save_messages(self):
        with open("social.json", "w") as file:
            json.dump([{"sender": msg.get_sender(), "receiver": msg.get_receiver(), "message": msg.get_message()} for msg in self.__messages], file)

    def load_messages(self):
        try:
            with open("social.json", "r") as file:
                messages = json.load(file)
                self.__messages = [Message(m['sender'], m['receiver'], m['message']) for m in messages]
        except FileNotFoundError:
            self.__messages = []

    def get_visited_messages(self, receiver):
        return [message for message in self.__messages if message.get_visited()]

    def check_messages(self, receiver):
        read = []
        for message in self.__messages:
            if not message.get_visited() and message.get_receiver() == receiver:
                message.set_visited(True)
                read.append(message.get_message())
        return read

message_manager = Message_manager()
message_manager.add_message("ilia", "mmd", "hi")
print(message_manager.check_messages("mmd"))
print(message_manager.check_messages("mmd"))
