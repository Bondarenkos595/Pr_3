import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

users = {
    "ivan123": {
        "password": hash_password("mypASSword"),
        "name": "Іваненко Іван Іванович"
    },
    "olga456": {
        "password": hash_password("securepASS"),
        "name": "Петренко Ольга Петрівна"
    }
}

def verify_user(login):
    if login in users:
        password_input = input("Введіть пароль: ")
        password_hash = hash_password(password_input)
        if password_hash == users[login]["password"]:
            print(f"Вітаємо, {users[login]['name']}! Успішний вхід.")
        else:
            print("Невірний пароль.")
    else:
        print("Користувача не знайдено.")

user_login = input("Введіть логін: ")
verify_user(user_login)
