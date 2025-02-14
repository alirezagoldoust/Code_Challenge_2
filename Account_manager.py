import json

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
    
    def signup(self, username, password):
        for user in self.__user_list:
            if user.get_username() == username:
                return False
            else:
                self.add_user(username, password)
                return True
            
    def login(self, username, password):
        for user in self.__user_list:
            if user.get_username() == username and user.get_password() == password:
                return user
            else:
            
                return None
            

class Menu_list :
    def __init__(self):
        self.account_manager = Account_manger()
        self.__active_user =  None
    
    def menu(self):
        while self.__active_user == None:
            print("1.login")
            print("2.signup")
            print("what is your choice? ")
            choice = int(input())
            if choice == 1:
                self.login()
            if choice == 2 :
                self.signup()
        if self.__active_user != None:
            print("1.follow")
            print("2.followers list")
            print("3.following list")
            print("4.messeage")
            choice = int(input())
            if choice == 1:
                followed_username = input("who you want to follow? ")
                
            if choice == 2 :
                self.signup()

            if choice == 3:

            if choice == 4:   
             

            

    def login(self):
        username = input()
        password = input()

        self.__active_user = self.account_manager.login(username, password)
        if not self.__active_user:
            print("wrong username")
