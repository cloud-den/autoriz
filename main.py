import os
from cryptography.fernet import Fernet


def write_key(filename="key.key"):
    if not os.path.exists(filename):
        key = Fernet.generate_key()
        with open(filename, "wb") as key_file:
            key_file.write(key)
        print(f"Ключ сохранён в файл: {filename}")
    else:
        print(f"Файл {filename} уже существует. Ключ не перезаписан.")


def load_key(filename = "key.key"):
    with open(filename, "rb") as key_file:
      return key_file.read()


def add(f, filename = "passwords.txt"):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    encrypted_password = f.encrypt(password.encode()).decode()
    with open(filename, "a") as file:
        file.write(f"{login}|{encrypted_password}\n")


def view(f, filename = "passwords.txt"):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return
    with open(filename, "r") as file:
        for line in file:
            login, encrypted_password = line.strip().split("|")
            decrypted_password = f.decrypt(encrypted_password.encode()).decode()
            print(f"Логин: {login}, Пароль: {decrypted_password}")

if __name__ == "__main__":
    write_key()
    key = load_key()
    f = Fernet(key)
    
    while True:
        choice = input("Выберите действие: [1] Добавить новые данные [2] Показать все данные [3] Выход: ")
        if choice == "1":
            add(f)
        elif choice == "2":
            view(f)
        elif choice == "3":
            break
        else:
            print("Неверный ввод.")
