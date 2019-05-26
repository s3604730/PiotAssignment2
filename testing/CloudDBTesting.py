from classList.User import User
from database import Database
import unittest
import os
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


class CloudDBTesting(unittest.TestCase):
    user = User("user123", "abc123", "John", "Doe", "johndoe@test.com")
    db = Database(testing=True)

    def test_insertUser(self):
        self.db.clearTable("LmsUser")
        print("------TESTING INSERT USER METHOD-------")
        res = self.db.insertUser(self.user.getUsername())
        self.assertEqual(res, True, "Should return True")

    def test_getUserIDByUserName(self):
        self.db.clearTable("LmsUser")
        print("------TESTING GET USER ID BY USERNAME METHOD-------")
        self.db.insertUser(self.user.getUsername())
        res2 = self.db.getUserIDByUserName(self.user.getUsername())
        self.assertTrue(res2 != "None", "Should not return None")

    def test_getUserIDByUserName_None(self):
        self.db.clearTable("LmsUser")
        print("------TESTING GET USER ID BY USERNAME (None case) METHOD-------")
        self.db.insertUser(self.user.getUsername())
        res2 = self.db.getUserIDByUserName("some username not existing")
        self.assertTrue(res2 == "None", "Should return None")


if __name__ == '__main__':
    unittest.main()
