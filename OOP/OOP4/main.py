class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.following = 0
        self.followers = 0
        # 'self.followers' It is not passed as a parameter to the constructor
        # meaning every User object will start with 0 followers by default.

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('01', 'Bolas')
user_2 = User('02', 'Bolitas')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)