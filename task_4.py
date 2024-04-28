def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Контакт {name} додано з номером {phone}.")

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Номер телефону для {name} змінено на {phone}.")
    else:
        print(f"Контакт {name} не знайдено.")

def show_phone(contacts, name):
    if name in contacts:
        print(f"Номер {name}: {contacts[name]}")
    else:
        print(f"Контакт {name} не знайдено.")

def show_all_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Список контактів порожній.")

def main():
    contacts = {}
    print("Введіть команду (add, hello, change, phone, all, exit):")
    
    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)
        
        if command == 'exit' or command == 'close':
            print("Програма завершує роботу.")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add' and len(args) == 2:
            add_contact(contacts, args[0], args[1])
        elif command == 'change' and len(args) == 2:
            change_contact(contacts, args[0], args[1])
        elif command == 'phone' and len(args) == 1:
            show_phone(contacts, args[0])
        elif command == 'all' and len(args) == 0:
            show_all_contacts(contacts)
        else:
            print("Невірно введена команда або аргументи.")

if __name__ == '__main__':
    main()