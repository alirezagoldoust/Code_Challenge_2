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

    def check_follower(self, user):
        return [
            connection.get_followed()
            for connection in self.__list_connection
            if connection.get_follower() == user
        ]

    def check_followed(self, followed):
        return [
            connection.get_follower()
            for connection in self.__list_connection
            if connection.get_followed() == followed
        ]

    def get_mutual_connection(self, user_1):
        l1 = self.check_follower(user_1)
        l2 = self.check_followed(user_1)
        return [user for user in l1 if user in l2]
