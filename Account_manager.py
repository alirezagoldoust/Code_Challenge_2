import json
from connect import Message_manager , Message
from social import Connection_Manager
class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
    
    def get_username(self):
        return self.__username
    
    def set_username(self, username: str):
        self.__username = username
        
    def get_password(self):
        return self.__password
    
    def set_password(self, password: str):
        self.__password = password
    
    def print(self):
#         print("Name:", self.__username, "Number:", self.__password, sep="\t")
        print(f"Name: {self.__username}\tNumber: {self.__password}")
    


class Account_manger:
    def __init__(self):
        self.__user_list = []

    def add_user(self, username:str, password:str):
        new_user = User(username= username, password=password)
        self.__user_list.append(new_user)
        return new_user
    
    def signup(self, username, password):
        # for user in self.__user_list:
        #     if user.get_username() == username:
        #         return False
        #     else:
        new_user = self.add_user(username, password)
        return new_user
            
    def login(self, username, password):
        for user in self.__user_list:
            if user.get_username() == username and user.get_password() == password:
                return user
            else:
            
                return None
            

class Menu_list :
    def __init__(self):
        self.account_manager = Account_manger()
        self.message_manager = Message_manager()
        self.connection_manager = Connection_Manager()

        self.__active_user =  None
    
    def menu(self):
        while self.__active_user == None:
            print("1.login")
            print("2.signup")
            print("what is your choice? ")
            choice = int(input())
            if choice == 1:
                user_name = input("what is your username? ")
                pass_word = input("what is your password? ")
                user = self.account_manager.login(user_name, pass_word)
                if user != None:
                    self.__active_user = user
            if choice == 2 :
                user_name = input("what is your username? ")
                pass_word = input("what is your password? ")
                user = self.account_manager.signup(user_name, pass_word)
                if user != None:
                    self.__active_user = user
        if self.__active_user != None:
            print("1.follow")
            print("2.followers list")
            print("3.following list")
            print("4.messeage")
            print("5.my messages")
            choice = int(input())
            if choice == 1:
                followed_username = input("who you want to follow? ")
                self.connection_manager.add_connection(self.__active_user.get_username(), followed_username)
                
            if choice == 2 :
                follower = self.connection_manager.check_follower(self.__active_user.get_username())
                for i, user in enumerate(follower):
                    print(f"{i}. {user}")

            if choice == 3:
                follwing = self.connection_manager.check_followed(self.__active_user.get_username())
                for i, user in enumerate(follwing):
                    print(f"{i}. {user}")

            if choice == 4:  
                follwing = self.connection_manager.get_mutual_connection(self.__active_user.get_username())
                for i, user in enumerate(follwing):
                    print(f"{i}. {user}")
                username_message = input("who you want to send the message? ") 
                mess = input("write your message")
                self.message_manager.add_message(self.__active_user.get_username(), username_message, mess)

            if choice == 5 :
                list_messages = self.message_manager.check_messages(self.__active_user.get_username())
                for mess in list_messages :
                    mess: Message
                    print(f"{mess.get_sender()}->{mess.get_message()}")
            

    def login(self):
        username = input()
        password = input()
        self.__active_user = self.account_manager.login(username, password)
        if not self.__active_user:
            print("wrong username")


