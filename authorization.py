from main import load_key
from cryptography.fernet import Fernet
import os


key = load_key()
f = Fernet(key)

def authorization(f, filename="passwords.txt"):
    while True:
        login_input = input("Введите логин: ")
        password_input = input("Введите пароль: ")

        if not os.path.exists(filename):
            print("Файл с паролями не найден.")
            return
        
        with open(filename, "r") as file:
            for line in file:
                login, encrypted_password = line.strip().split("|")
                if login == login_input:
                    try:
                        decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                        if decrypted_password == password_input:
                            print("Авторизация успешна!")
                            return
                        else:
                            print("Неверный пароль.")
                            break
                    except:
                        print("Ошибка при расшифровке пароля.")
                        break
            else:
                print("Логин не найден.")



if __name__ == "__main__":
    authorization(f)
