from loguru import logger
from cryptography.fernet import Fernet
from view import user_menu


def controller():
    logger.info("Контроллер создан")

    KEY = Fernet.generate_key()
    cipher = Fernet(KEY)

    line = user_menu()
    logger.info(F"В переменной line: {line}")
    if line[1] == 1:
        result = dobavlenie(line[0])
    elif line[1] == 2:
        result = udalenie(line[0])
    elif line[1] == 3:
        result = pereschet(line[0])
    elif line[1] == 4:
        result = izmenenie(line[0])
    else:
        logger.error("Буянит батюшка")
    


def dobavlenie(text, cipher):
    return cipher.dobavlenie(text.dobavlenie()).decode()

def udalenie(text, cipher):
    pass

def pereschet(text, cipher):
    pass

def izmenenie(text, cipher):
    pass
