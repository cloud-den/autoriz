import os
from cryptography.fernet import Fernet
from main import load_key


key = load_key()
f = Fernet(key)

def authorization(login, password, f, filename = "passwords.txt"):
    if not os.path.exists(filename):
        return False
        
    with open(filename, "r") as file:
        for line in file:
            login, encrypted_password = line.strip().split("|")
            if input_login == login:
                decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                return decrypted_password == password
    return False

while True:
    input_login = input("Введите логин: ").strip()
    input_password = input("Введите пароль: ").strip()
    if authorization(input_login, input_password, f):
        print("Авторизация успешна!")
        break
    else:
        print("Ошибка: неверный логин или пароль")

if __name__ == "__main__":
    authorization(input_login, input_password, f, filename = "passwords.txt")
