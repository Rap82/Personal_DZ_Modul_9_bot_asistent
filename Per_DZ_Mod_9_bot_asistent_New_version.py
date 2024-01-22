def input_error(func):
    def inner(user_input):
        list_user_input = user_input.lower().strip().split()
        try:
            result = func(user_input)
            if result in  massages_dict.keys():
                return result
        except IndexError as massage:
            command = list_user_input[0]
            if command in ('add', "change"):
                massage = f"{YLLOW_TEXT}Невірні параметри для команди {GREEN_TEXT}{command}{YLLOW_TEXT} !!!.\n\
                {RED_TEXT}# Приклад {GREEN_TEXT}{command}{BIRUZA_TEXT} Імя_контакту{YLLOW_TEXT} Номер_телефону {DEFALUT_TEXT} "
            else:
                massage = f"{YLLOW_TEXT}Невірні параметри для команди {GREEN_TEXT}{command}{YLLOW_TEXT} !!!.\n\
                {RED_TEXT}# Приклад {GREEN_TEXT}{command}{BIRUZA_TEXT} Імя_контакту{YLLOW_TEXT} "
            return massage
        except KeyError:
            return BAD_COMMAND_MESSAGE
        except ValueError:
            return f"{YLLOW_TEXT}Номер може містити тільки цифри !!!\n{RED_TEXT}# Приклад - 0931245891{DEFALUT_TEXT}"
        except TypeError as massage:
            massage = f"{YLLOW_TEXT}{massage}{PISKAZKA_SHOW_ALL}"
            return massage
        return result
    return inner


def bad_comand(user_input):
    return f'{YLLOW_TEXT}Tака команда не пітримується наразі\n{DEFALUT_TEXT}{DOSTUPNI_COMANDY}'

@input_error
def hello_answer(user_input):
    return f'{YLLOW_TEXT}{HELLO_ANSWER}{DEFALUT_TEXT}'

@input_error
def show_all_contacts(user_input):
    return_contacts_str = f'{GREEN_TEXT}{"Name":<10}  {"Phone":<12}{YLLOW_TEXT}\n\n'
    for name , phone in phone_book.items():
        return_contacts_str += f'{BIRUZA_TEXT}{name.capitalize():<10}  {YLLOW_TEXT}{phone:<12} \n'
    return return_contacts_str

@input_error
def add_new_contact(user_input):
    list_user_input = user_input.lower().strip().split()

    name = list_user_input[1].capitalize()
    phone = int(list_user_input[2])
    phone = list_user_input[2]
    if phone_book.get(name) is None and len(phone) == 10:
        phone_book[name] = phone
            
        return "add_new_contact_ok"
    if len(phone) != 10:
            return "add_new_contact_phone_false"
    raise TypeError("У вас вже є контакт з таким іменем !!!")


@input_error
def print_phone(user_input):
    list_user_input = user_input.lower().strip().split()
    name = list_user_input[1].capitalize()
    phone = phone_book.get(name)
    if phone is not None:
        finded_contact = f'{YLLOW_TEXT}За вказаним іменем {BIRUZA_TEXT}{name.capitalize()}{YLLOW_TEXT} знайдено номер{BIRUZA_TEXT} {phone}{DEFALUT_TEXT}'
        return finded_contact
    else :
        raise TypeError("Такого іменні не знайдено у вашій телефоній книзі !!!")
@input_error
def new_phone(user_input):
    list_user_input = user_input.lower().strip().split()
    name = list_user_input[1].capitalize()
    phone = int(list_user_input[2])
    phone = list_user_input[2]
    if phone_book.get(name) is not None and len(phone) == 10:
        phone_book[name] = phone
        return "change_new_contact_ok"
    if len(phone) !=10:
        return "add_new_contact_phone_false"
    raise TypeError("Такого іменні не знайдено у вашій телефоній книзі !!!")

@input_error
def good_bye(user_input):
    return f"{YLLOW_TEXT}Good bye!{DEFALUT_TEXT}"
     
ACTIONS = {
    'hello': hello_answer,
    'show all': show_all_contacts,
    'add': add_new_contact,
    'phone': print_phone,
    'change': new_phone,
    'exit': good_bye,
    'good bye': good_bye,
    'close': good_bye,
    "bad_comand": bad_comand,
    }


def choice_action(user_input):
    user_input_comand = user_input.lower().strip()
    chek_comand = user_input.lower().strip().split() 
    for command in ACTIONS:
        if user_input_comand.startswith(command) and (chek_comand[0] in FOR_CHEK_LIST_COMANDS_BOT): 
            return ACTIONS[command]
    return bad_comand

       
# phone_book = {'Vassddffff': 0977854123, 'Der' : 0507856127, 'Cos' : 0667856452}
phone_book ={}

YLLOW_TEXT = "\033[33m"
GREEN_TEXT = "\033[32m"
RED_TEXT = "\033[31m"
DEFALUT_TEXT = "\033[0m"
PURPURE_TEXT = "\033[35m"
BIRUZA_TEXT = "\033[36m"

HELLO_ANSWER = "How can I help you?"
LIST_COMANDS_BOT = ["hello", "add", "change","phone","show all","good bye", "close", "exit"]
FOR_CHEK_LIST_COMANDS_BOT = ["hello", "add", "change","phone","show","good", "close", "exit"] # Модифікований список команд для додаткової перевірки .
DOSTUPNI_COMANDY = f"{RED_TEXT}Доступні наступні команди : {GREEN_TEXT}{LIST_COMANDS_BOT}{DEFALUT_TEXT}"
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN_TEXT}show all{YLLOW_TEXT} - покаже доступні контакти{DEFALUT_TEXT}"
BAD_COMMAND_MESSAGE = f"{YLLOW_TEXT}Tака команда не пітримується наразі\n{DEFALUT_TEXT}{DOSTUPNI_COMANDY}"
BAD_NAME_IN_PHONEBOOK = f"{YLLOW_TEXT}У вас немає контакту з таким іменем !!!\n{PISKAZKA_SHOW_ALL}"
massages_dict ={ 
    "add_new_contact_ok": f"{YLLOW_TEXT}Новий контакт успішно додано{PISKAZKA_SHOW_ALL}",
    "add_new_contact_phone_false": f"{YLLOW_TEXT}Номер телефону має містити 10 цифр !!!\n{RED_TEXT}# Приклад - 0931245891{DEFALUT_TEXT}",
    "bad_name_in_phonebook": BAD_NAME_IN_PHONEBOOK ,
    "change_new_contact_ok" : f"{YLLOW_TEXT}Номер телефону успішно змінено{PISKAZKA_SHOW_ALL}"
    }

print(f'\n{YLLOW_TEXT}Вас вітає Бот для роботи з вашии контактами.')
print(f'{RED_TEXT}Доступні наступні команди : {GREEN_TEXT}{LIST_COMANDS_BOT}{DEFALUT_TEXT}')


def main():
    while True :
        user_input = input(f"{PURPURE_TEXT}ВВедіть команду{DEFALUT_TEXT}\n")
        list_user_input = user_input.lower().strip().split() 
        
        if list_user_input == [] :
            print(f'{YLLOW_TEXT}Ви нічого не ввели \n{DOSTUPNI_COMANDY}')
            continue
        user_command = choice_action(user_input)
        result = user_command(user_input)
        if result in massages_dict:
            print(massages_dict[result])
        else :
            print(user_command(user_input))
        if result == f"{YLLOW_TEXT}Good bye!{DEFALUT_TEXT}":
            break

if __name__ == '__main__':
    main()