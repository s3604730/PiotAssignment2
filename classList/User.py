from classList.UserAbstract import UserSkeleton


class User(UserSkeleton):
    def __init__(self, username, password, firstName, lastName, email):
        super().__init__(username, password, firstName, lastName, email)
