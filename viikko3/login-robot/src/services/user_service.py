from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        elif len(username) < 3 or len(password) < 8:
            raise UserInputError("Username or password not long enough.")
        elif not re.search("^[a-z]+$", username) or not re.search("[^a-z]",password):
            raise UserInputError("Check your characters.")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists.")
        
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
