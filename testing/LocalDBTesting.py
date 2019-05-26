from classList.User import User
from classList.Database import Database
import unittest
import os
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


class LocalDBTesting(unittest.TestCase):
    user = User("user123", "abc123", "John", "Doe", "johndoe@test.com")
    db = Database(testing=True)

    def test_insertUser(self):
        self.db.clearDatabase()
        print("------TESTING INSERT USER METHOD-------")
        res = self.db.insertUser(self.user)
        self.assertEqual(res, True, "Should return True")

    def test_findUserByUsername(self):
        self.db.clearDatabase()
        print("------TESTING FIND USER BY USERNAME METHOD-------")
        self.db.insertUser(self.user)
        username = "user123"
        res2 = self.db.findUserByUsername(username)
        self.assertEqual(res2[1], username, "Should return true")

    def test_findUserByUsernameAndPassword(self):
        self.db.clearDatabase()
        print("------TESTING FIND USER BY USERNAME AND PASSWORD METHOD-------")
        self.db.insertUser(self.user)
        res3 = self.db.findUserByUsernameAndPassword(
            self.user.getUsername(), self.user.getPassword())
        self.assertEqual(res3[1], self.user.getUsername(),
                         "Should return true")
        self.assertEqual(res3[2], self.user.getPassword(),
                         "Should return true")


if __name__ == '__main__':
    unittest.main()
