class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.friends = []

    def setName(self, new_name):
        self.name = new_name


    def setUserName(self, new_username):
        self.name = new_username

    def addFriend(self, new_friend):
        self.friends.append(new_friend)


class Network:
    # Define the fields and methods for your object here.
    def getName(self):
        return self.name

    def getUsername(self):
        return self.username

    def getFriends(self):
        return self.friends


def main():
    # Define the program flow for your user interface here.
    user1 = User
    print("Press 'n' to set your name.")
    print("Press 'u' to set your username.")
    if input == 'n':
        print("Name: ")
        input = new_name
        setName(user1, new_name)
    if input == 'u':
        print("Username: ")
        input = new_username
        setUsername(user1, new_username)
    
    print (getName(user1), getUsername(user1))

# Runs your program.
if __name__ == '__main__':
    main()
