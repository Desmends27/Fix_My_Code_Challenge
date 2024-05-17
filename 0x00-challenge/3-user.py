#!/usr/bin/python3
"""
User Model with password hashing (comments removed)
"""
import hashlib
import uuid


class User:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            self._password = None
        else:
            raise NotImplementedError

    def is_valid_password(self, pwd):
        if pwd is None or not isinstance(pwd, str) or self._password is None:
            return False
        raise NotImplementedError


if __name__ == "__main__":
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    user_1.password = "placeholder"
    if user_1.password != "placeholder":
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password("placeholder"):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
