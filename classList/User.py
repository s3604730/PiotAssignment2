from UserAbstract import UserSkeleton


class User(UserSkeleton):
    def __init__(self, userName, passWord, firstName, lastName, email):
        super().__init__(userName, passWord, firstName, lastName, email)
