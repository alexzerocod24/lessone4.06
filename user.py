class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'пользователь'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'Администратор'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f'Пользователь {user.get_name()} добавлен.')
        else:
            print('Такого пользователя нет.')

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f'Пользователь {user.get_name()} удалён.')
                return
        print('Пользователь не найден.')


# Пример использования
if __name__ == "__main__":
    # Создаем пользователей
    user1 = User(1, "Андрей")
    user2 = User(2, "Владимир")
    user3 = User(3, "Ольга")

    # Создаем администратора
    admin = Admin(57, "Иван")

    # Список пользователей
    user_list = [user1, user2, user3]

    # Выводим список пользователей
    print("Initial user list:")
    for user in user_list:
        print(f'{user.get_user_id()}: {user.get_name()} - {user.get_access_level()}')

    # Администратор добавляет нового пользователя
    new_user = User(4, "Татьяна")
    admin.add_user(user_list, new_user)

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 2)

    # Выводим обновленный список пользователей
    print("\nUpdated user list:")
    for user in user_list:
        print(f'{user.get_user_id()}: {user.get_name()} - {user.get_access_level()}')