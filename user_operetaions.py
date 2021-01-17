from user import User
from user_dao import UserDao


class UserOperaetions:
    def __init__(self):
        pass

    def validate_user_exist(self, user_name_input):
        user_name_dao = UserDao()
        user_name_value = user_name_dao.get_user_name()

        for user_name in user_name_value:
            if user_name_input != user_name:
                return False
            return True

    def create_user(self, user_name, password, adv_key):
        users = [User(user_name, password, adv_key)]

        return users
