class Connection:
    def __init__(self, follower, followed):
        self.__follower = follower
        self.__followed = followed
        
    def get_follower(self):
        return self.__follower
    
    def get_followed(self):
        return self.__followed


class Connection_Manager:
    def __init__(self):        
        self.__list_connection = []

    def add_connection(self, follower, followed):
        self.__list_connection.append(Connection(follower, followed))

    def check_follower(self, follower, followed):
        for user in self.__list_connection:
            
