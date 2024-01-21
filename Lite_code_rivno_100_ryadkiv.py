phone_book = {}

def input_error(func):
    def hundler(data):
        try:
            result = func(data)
        except IndexError as massage:
            massage ="Input corect parametrers of comand!!!"
            return massage
        except TypeError as massage:
            massage ="Input corect data !!!"
            return massage
        return result
    return hundler

@input_error
def hello(data):
    return "How can I help you?"

def bad_comand(data):
    return "Input corect comand!!!"
@input_error
def show_all(data):
    return_contacts_str = ""    
    for name , phone in phone_book.items():
        return_contacts_str += f'{name.capitalize():<10}  {phone:<12} \n'
    return return_contacts_str

@input_error
def add(data):
    list_user_input = data.lower().strip().split()
    some_dict = {}
    name = list_user_input[1].capitalize()
    
    phone = list_user_input[2]
    if phone_book.get(name) is None :
        some_dict[name] = phone
        phone_book.update(some_dict)
        return "Contact add successfully"
    raise TypeError

@input_error
def phone(data):
    list_user_input = data.lower().strip().split()
    name = list_user_input[1].capitalize()
    phone = phone_book.get(name)
    if phone is not None:
        finded_contact = f'Знайдено {phone}'
        return finded_contact
    else :
        raise TypeError
@input_error
def change(data):
    list_user_input = data.lower().strip().split()
    name = list_user_input[1].capitalize()
    
    phone = list_user_input[2]
    if phone_book.get(name) is not None :
        phone_book[name] = phone
        return "Contact change successfully"
    
    raise TypeError
@input_error
def good_bye(data):
    return "Good bye!"

ACTIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': good_bye,
    'close': good_bye,
    'exit': good_bye,
}

@input_error
def choice_action(data):
    for command in ACTIONS:
        if data.startswith(command):
            return ACTIONS[command]
    return bad_comand
 
def main():
    while True:
        data = input('Input comand\n')
        list_user_input =data.lower().split()
        func = choice_action(data)
        if list_user_input == [] :
            print(f'Input nothing \n')
            continue
        result = func(data)
        print(result)
        if result == 'Good bye!':
            break

if __name__ == '__main__':
    main()