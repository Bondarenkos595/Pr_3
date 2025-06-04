import sqlite3
import hashlib

DB_NAME = "users.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def add_user(login, password, full_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                       (login, hash_password(password), full_name))
        conn.commit()
        print(" Користувача додано успішно.")
    except sqlite3.IntegrityError:
        print(" Користувач з таким логіном вже існує.")
    finally:
        conn.close()

def update_password(login, new_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE login = ?",
                   (hash_password(new_password), login))
    if cursor.rowcount == 0:
        print(" Користувача не знайдено.")
    else:
        print("Пароль оновлено.")
    conn.commit()
    conn.close()

def authenticate_user(login):
    password = input("Введіть пароль: ")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE login = ?", (login,))
    row = cursor.fetchone()
    conn.close()

    if row:
        hashed_input = hash_password(password)
        if hashed_input == row[0]:
            print("Автентифікація успішна.")
        else:
            print("Невірний пароль.")
    else:
        print("Користувача не знайдено.")

if __name__ == "__main__":
    initialize_db()

    print("Виберіть опцію:")
    print("1 - Додати користувача")
    print("2 - Оновити пароль")
    print("3 - Автентифікація")

    choice = input("Ваш вибір: ")

    if choice == '1':
        login = input("Логін: ")
        password = input("Пароль: ")
        full_name = input("Повне ПІБ: ")
        add_user(login, password, full_name)

    elif choice == '2':
        login = input("Логін користувача: ")
        new_password = input("Новий пароль: ")
        update_password(login, new_password)

    elif choice == '3':
        login = input("Логін користувача: ")
        authenticate_user(login)

    else:
        print("Невірний вибір.")
