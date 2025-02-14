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

    def check_follower(self, follower):
        [connection.get_followed() for connection in self.__list_connection if connection.get_follower() == follower]
        
    def check_followed(self, followed):
        [connection.get_follower() for connection in self.__list_connection if connection.get_followed() == followed]
        
    def mutual_connection(self, follower_list, followed_list):
        [mutual for mutual in  if follower_list[mutual] == followed_list[mutual]]
