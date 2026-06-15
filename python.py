# __init__
# __str__

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Пользователь {self.name}"

user = User("Алишер")

print(user.name)
print(user)

# class User:
#     pass
# user = User()
# print(user)