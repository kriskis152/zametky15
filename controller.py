from loguru import logger
from cryptography.fernet import Fernet
from view import user_menu


def controller():
    logger.info("Контроллер создан")

   # KEY = Fernet.generate_key()
   # cipher = Fernet(KEY)

    line = user_menu()
    logger.info(F"В переменной line: {line}")
    if line[1] == 1:
        result = dobavlenie(line[0])
        logger.info(result)
    elif line[1] == 2:
        result = udalenie(line[0])
    elif line[1] == 3:
        result = pereschet(line[0])
    elif line[1] == 4:
        result = izmenenie(line[0])
    else:
        logger.error("Буянит батюшка")
    


def dobavlenie(text):
    filename = "notes.txt"
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text + "\n")
        return F"Заметка успешно создана, можешь посмотреть в файле {filename}"
    except Exception as e:
        return F"Ошибкка"


def udalenie(note_number):
    filename = "notes.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines =f.readlines()
            index = note_number -1
            if index < len(lines):
                delete_note = lines.pop(index).strip()
                with open(filename, 'w', encoding="utf-8") as f:
                    f.writelines(lines)
                return f"Заметку {note_number} удалил"
            else:
                return F"Ошибка, всего заметок {len(lines)}"
    except Exception as e:
        return F"Ошибка"



def pereschet(text):
    pass

def izmenenie(text):
    pass
