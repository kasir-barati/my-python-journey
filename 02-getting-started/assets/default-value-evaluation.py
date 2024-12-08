def create_user(username, user={}):
    user["username"] = username
    return user

user1 = create_user("hua")
user2 = create_user("tibet")
user3 = create_user('sarah')

print(user1, user2, user3)

def create_user(username, user=None):
    user = user or {}
    user["username"] = username
    return user

user1 = create_user("hua")
user2 = create_user("tibet")
user3 = create_user('sarah')

print(user1, user2, user3)

