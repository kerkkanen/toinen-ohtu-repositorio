from entities.user import User


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
        if len(username) < 2 or len(username) > 15:
            raise UserInputError("Username length must be between 2-15")

        number = False
        symbol = False

        if len(password) < 4 or len(password) > 30:
            raise UserInputError("Password length must be at least 8")
        for i in password:
            if i in "0123456789":
                number = True
                break
            if i not in "0123456789abcdefghijklmnopqrstuvwxyz":
                symbol = True
                break
        if not number:
            raise UserInputError("Password must contain at least one number")
        if symbol:
            raise UserInputError("Password must contain only numbers or letters")
