
#                           '''Завдання '''

# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури,
# і відповідати відповідно до введеної команди.

# Бот помічник повинен стати для нас прототипом додатка-асистента.
# Додаток-асистент в першому наближенні повинен уміти працювати з книгою контактів і календарем.
# У цій домашній роботі зосередимося на інтерфейсі самого бота.
# Найбільш простий і зручний на початковому етапі розробки інтерфейс -
# це консольний додаток CLI (Command Line Interface).
# CLI досить просто реалізувати. Будь-який CLI складається з трьох основних елементів:

# Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків,
# виділення з рядка ключових слів та модифікаторів команд.
# Функції обробники команд — набір функцій, які ще називають handler,
# вони відповідають за безпосереднє виконання команд.
# Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних
# та повернення користувачеві відповіді від функції-handlerа.
# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону,
# знаходити номер телефону за ім'ям,
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг.
# Щоб реалізувати таку нескладну логіку,
# скористаємося словником. У словнику будемо зберігати ім'я користувача
# як ключ і номер телефону як значення.

# Умови
# Бот повинен перебувати в безкінечному циклі, чекаючи команди користувача.
# Бот виведе у консоль "Good bye!" і завершує свою роботу,
# якщо зустрічає слова: "good bye", "close", "exit"  .
# Бот не чутливий до регістру введених команд.
# Бот приймає команди:
# "hello", відповідає у консоль "How can I help you?"
# "add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт.
# Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
# "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту.
# Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
# "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
# Замість ... користувач вводить ім'я контакту, чий номер треба показати.
# "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
# "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу
# після того, як виведе у консоль "Good bye!".
# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
# Цей декоратор відповідає за повернення користувачеві повідомлень виду "Enter user name",
# "Give me name and phone please" і т.п.
# Декоратор input_error повинен обробляти винятки,
# що виникають у функціях-handler (KeyError, ValueError, IndexError)
# та повертати відповідну відповідь користувачеві.
# Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один
# або декілька рядків та повертають рядок.
# Вся логіка взаємодії з користувачем реалізована у функції main,
#всі print та input відбуваються тільки там

# ======================= Алгоритм   ==========================

''' Алгоритм : Будемо, від користувача, з клавіатури приймати запити,
в вигляді визначенмх команд, а також введених даних; обробляти в визначений спосіб\
і повертати їх результат користувачу. Все як описано в умоваг завдання.
Примітка : Оскільки всі print і input - відбуваються в середені main()
    то з всіх функції будемо повертати дані, а не принтити їх відразу. 
    Код можливо оптимізувати, якщо включити обмеження на print і input \
    і повернення з функції виключно рядка  '''

# ++++++++++++++++++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++


def input_error(func):
    '''Декоратор - згідно умов завдання .\
    Буде повертати результати обробки введних даних користувачем\
    Примітка : оскільки всі print і input мають відбуватись в основній функції 
    то декоратор застусуємо до проміжних функціїй *parser_comand_result(comand_output) \
    і *hendler_result(result) які будуть містити результати в вбудованих *parser_comand(user_input)
    і *hendler(comand_output_result, full_list_dicts_contact) - відповідно.'''
    def inner(result):
        try:
            result = func(result)
            # print(result)
            match result :
                case 'exit' :
                    return result
                case 'no_input':
                    raise TypeError
                case None:
                    raise IndexError
                case 'KeyError' :
                    raise KeyError
                case 'IndexError':
                    raise IndexError
                case 'ValueError':
                    raise ValueError
                case "add":
                    return '''\033[33mНевірні параметри для команди \033[32m"add" \033[33m!!!.\n\
                \033[31m# Приклад \033[32m add \033[33mімя_контакту номер_телефону\033[0m'''
                case "change":
                    return '''\033[33mНевірні параметри для команди \033[32m"change" \033[33m!!!.\n\
                    \033[31m# Приклад \033[32m change \033[33mімя_контакту номер_телефону\033[0m'''
                case "phone":
                    return '''\033[33mНевірні параметри для команди \033[32m"phone" \033[33m!!!.\n\
                \033[31m# Приклад \033[32m phone \033[33mімя_контакту \033[0m'''
                case _ :
                    return f'\n\033[33m{result}\033[0m'
        except IndexError:
            return f'\033[33mTака команда не пітримується наразі. \
                \n\033[0m{DOSTUPNI_COMANDY}'
        except KeyError :
            return '''\033[33mВказаного імені немає в вашій телефоній книзі \n\
                Скористайтесь командою  \033[32m show all\033[33m - \
                для перегляду збережених контактів\033[0m '''
        except ValueError:
            return "Номер може містити тільки цифри !!!\n\033[31m# Приклад - 0931245891\033[0m"
        except TypeError:
            return f"Ви нічого не ввели !!!\n{DOSTUPNI_COMANDY}"
    return inner
@input_error
def hendler_result(result):
    '''Проміжна функція яка буде мати результати повернуті з \
        *hendler(comand_output_result, full_list_dicts_contact)'''
    return result
@input_error
def parser_comand_result(comand_output):
    '''Проміжна функція яка буде мати результати повернуті з *parser_comand(user_input)'''
    return comand_output


def parser_comand(user_input):
    '''Допоміжна функція що відповідає за аналіз введних даних з клавіатури користувачем \
    Вичлененя з них команд і відповідних параметрів 
    Аналіз їх на валідність і поверненя нормалізованих команд і даних з функції\
     для подальшої обробки в хендлері.'''
    list_user_input = []
    fixe_comand_and_value_user_input = []

    FILTER_WORD = ["hello", "add", "change","phone", "close", "exit"]
    LIST_EXIT = ["good bye", "close", "exit"]

    list_user_input = user_input.lower().strip().split()
    kilkist_element_in_list_user_input = len(list_user_input)

    try:
        if kilkist_element_in_list_user_input == 0 :
            return 'no_input'

        elif kilkist_element_in_list_user_input == 1 :

            if list_user_input [0] in  FILTER_WORD :

                if list_user_input [0] in LIST_EXIT :
                    return "bot_exit"

                elif list_user_input[0] == 'hello':
                    return "hello_answer"
                else :
                    return f'{list_user_input [0]}'

        elif  kilkist_element_in_list_user_input >= 2 :
            if list_user_input[0] == 'good' and list_user_input[1]=='bye':
                return "bot_exit"

            elif list_user_input[0] == 'show' and list_user_input[1]=='all':
                return  "show_all_contacts"

            elif list_user_input[0] == "phone":
                list_user_input[0] = "print_phone"
                fixe_comand_and_value_user_input.append(list_user_input[0])
                fixe_comand_and_value_user_input.append(list_user_input[1])
                return fixe_comand_and_value_user_input

            elif list_user_input[0] == "change" and kilkist_element_in_list_user_input >=3:
                list_user_input[0] = "new_phone"

                fixe_comand_and_value_user_input.append(list_user_input[0])
                fixe_comand_and_value_user_input.append(list_user_input[1])
                fixe_comand_and_value_user_input.append(list_user_input[2])
                return fixe_comand_and_value_user_input

            elif list_user_input[0] == "add" and kilkist_element_in_list_user_input >=3:
                list_user_input[0] = "add_new_contact"
                fixe_comand_and_value_user_input.append(list_user_input[0])
                fixe_comand_and_value_user_input.append(list_user_input[1])
                fixe_comand_and_value_user_input.append(list_user_input[2])

                return fixe_comand_and_value_user_input

            elif list_user_input[0] == "add" and kilkist_element_in_list_user_input <3:
                return "add"

            elif list_user_input[0] == "change" and kilkist_element_in_list_user_input <3:
                return "change"

            else :

                if list_user_input[0] == 'hello':
                    return "hello_answer"

                elif list_user_input [0] in  FILTER_WORD :

                    if list_user_input [0] in LIST_EXIT :

                        return "bot_exit"

    except KeyError :
        return 'KeyError'
    except ValueError :
        return 'ValueError'
    except IndexError :
        return 'IndexError'

def hendler(comand_output_result, full_list_dicts_contact):
    '''Допоміжна функція в якій будемо обробляти дані переданні з частини коду\
     що відповідає за персер команд. 
     До отриманих даних будемо виконувати дії згідно переданих команд. '''

    filter_user_comand = comand_output_result

    def hello_answer(hello):
        hello = f'\n\033[33m{HELLO_ANSWER}\033[0m'
        return hello


    def bot_exit(flag_exit):
        flag_exit = "exit"
        return flag_exit


    def show_all_contacts(name, phone):
        curent_contact = f'{name.capitalize():<10}  {phone:<12} \n'
        return curent_contact

    def add_new_contact(name, phone):

        if len(phone) == 10 and phone.isdigit():
            new_contact = name.capitalize() +':'+ phone
            return new_contact

        else :
            if not phone.isdigit():
                return "Номер може містити тільки цифри"
            elif len(phone)!=10:
                return "Номер телефону має містити 10 цифр !!!\
                    \n\033[31m# Приклад - 0931245891\033[0m"

    def print_phone(name, curent_phone):
        if curent_phone == None :
            return "У вас немає контакту з таким іменем !!!\n\
            Команда - \033[32mshow all\033[33m - покаже доступні контакти\033[0m"

        else :
            finded_contact = f'За вказаним іменем \033[32m{name.capitalize()} \
                \033[33mзнайдено \033[32m{curent_phone}\033[0m'
            return finded_contact

    def new_phone(curent_name, add_new_phone):

        if curent_name in list(full_list_dicts_contact.keys()):
            if len(add_new_phone) == 10 and int(add_new_phone):
                full_list_dicts_contact[curent_name] = add_new_phone
                return f"Для \033[32m{curent_name}\033[33m \
                    номер телефону замінено на \033[32m{add_new_phone}\033[0m"
            else:
                return "номер телефону має містити 10 цифр !!!\
                    \n\033[31m# Приклад - 0931245891\033[0m"
        else :
            raise KeyError

    try :

        if isinstance(filter_user_comand, str):
            match filter_user_comand :
                case  None:
                    return None

                case "hello_answer" :
                    filter_user_comand = hello_answer(hello='')
                    return filter_user_comand

                case 'bot_exit':
                    filter_user_comand = bot_exit(flag_exit='')
                    return filter_user_comand

                case "show_all_contacts" :
                    return_contacts_str = '\033[32m{:<10} {:^10}\n\n\033[0m'.format("Name", "Phone")

                    for name , phone in full_list_dicts_contact.items():

                        return_contacts_str += show_all_contacts(name, phone)
                    return_contacts_str = f'\n{return_contacts_str}'
                    return return_contacts_str

        if isinstance(filter_user_comand, list):

            match filter_user_comand[0]:
                case 'add_new_contact' :
                    some_dict = {}
                    name = filter_user_comand[1]
                    phone = filter_user_comand[2]

                    if  name.capitalize() in list(full_list_dicts_contact.keys()) :
                        return "у вас вже є контакт з таким іменем !!!"
                    curent_user_input_list = add_new_contact(name, phone).split(':')

                    if len(curent_user_input_list)== 1 :
                        return curent_user_input_list[0]
                    else :
                        some_dict[curent_user_input_list[0]] = curent_user_input_list[1]
                        full_list_dicts_contact.update(some_dict)
                        return f'Новий контакт <{f'\033[32m{curent_user_input_list[0].capitalize()}'} - {f'{curent_user_input_list[1]}\033[33m'}> успішно додано'

                case 'print_phone' :
                    curent_phone = full_list_dicts_contact.get(filter_user_comand[1].capitalize())
                    name = filter_user_comand[1].capitalize()
                    return_contact_str = print_phone(name, curent_phone)
                    return return_contact_str


                case "new_phone" :
                    curent_name = filter_user_comand[1].capitalize()
                    add_new_phone = filter_user_comand[2]
                    return new_phone(curent_name, add_new_phone)

    except KeyError :
        return 'KeyError'
    except ValueError :
        return 'ValueError'
    except IndexError :
        return 'IndexError'
def main():
    '''Основна функція в якій будемо принтети результати віх допоміжних'''
    close = True
    while close :

        user_input = input('\n\033[35mВВедіть команду\n\033[0m')
        comand_output = parser_comand(user_input)

        if isinstance(comand_output, list):

            result = hendler(comand_output, full_list_dicts_contacts)
            print (hendler_result(result))

        elif comand_output in RETURN_LIST_COMANDS_BOT :

            result = hendler(comand_output, full_list_dicts_contacts)

            if  hendler_result(result) == "exit":

                print('\n\033[33mGood bye!\033[0m')
                close = False
                break

            else :
                print (hendler_result(result))
        else :
            print(f'\033[33m{parser_comand_result(comand_output)}\033[0m')

HELLO_ANSWER = "How can I help you?"

LIST_COMANDS_BOT = ["hello", "add", "change","phone","show all","good bye", "close", "exit"]

RETURN_LIST_COMANDS_BOT = ["hello_answer", 'add_new_contact', 'print_phone',
                           'print_phone',"show_all_contacts",'bot_exit']

DOSTUPNI_COMANDY = f'\033[31mНаразі доступні наступні команди : \033[32m{LIST_COMANDS_BOT}\033[0m'

print('\n\033[33mВас вітає Бот для роботи з вашии контактами. \033[0m :')
print(f'\033[31mДоступні наступні команди : \033[32m{LIST_COMANDS_BOT}\033[0m')

full_list_dicts_contacts = {'Vassddffff': 123455, 'Der' : 2222222222, 'Cos' : 55555555}

main() # Виклик основної функції.
