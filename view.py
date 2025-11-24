from loguru import logger 


def user_menu():
    logger.info("Дуралей зшёл в моё меню")
    print("Привет, добавь заметку!")
    print("Или удали одну")
    print("Или ничего не делай. Мне всё равно.")

    answer = "" 
    while True:
        print("Если хочешь добавить заметку нажми 1")
        print("Если хочешь удалить, то нажми 2")
        print("Если хочешь увидеть количество заметок нажми 3")
        print("Если хочешь изменить существующую, нажми 4")
        print("Если хочешь всё закончить... Жми 5!")
        answer = int(input("Что хочешь делать? "))
        if answer == 1:
            line  = user_input("Введи заметку: ")
            return [line, 1]
        elif answer == 2:
            line = user_input("Какую заметку нужно удалить (номер)")
            return [line, 2]
        elif answer == 3:
            pass # должна быть функция которая только выводит число, колличество заметок
        elif answer == 4:
            line = user_input("Введи номер заметки, которую хочешь поменять: ")
            return [line, 4]
        elif answer == 5:
            return
        else:
            print("Нормально разговаривай")





def user_input(settings):
    line = input(settings)
    return line

