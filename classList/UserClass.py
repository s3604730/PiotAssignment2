from UserAbstract import UserSkeleton 


class UserClass(UserSkeleton):
    def __init__(self, userName, passWord, firstName, lastName, email):
        super().__init__(userName, passWord, firstName, lastName, email)
        

