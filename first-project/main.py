from prettytable import PrettyTable


def print_menu() -> str:
    print('''Выберите опцию:
    1. Просмотреть список контактов.
    2. Добавить контакт.
    3. Редактировать контакт.
    4. Удалить контакт.
    5. Остановить работу программы.''')
    on_input: str = input('Введите выбор: ')
    return on_input


def load_contacts() -> list:
    try:
        with open('contacts.txt', 'r') as file:
            return [line.strip().split('|') for line in file.readlines()]
    except FileNotFoundError:
        with open('contacts.txt', 'w'):
            pass
        return []


def save_contacts(contacts: list) -> None:
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write('|'.join(contact) + '\n')


def display_contacts(contacts: list) -> None:
    if not contacts:
        print('Ваша контактная книга пуста.')
    else:
        print('Ваша контактная книга:')
        table = PrettyTable()
        table.field_names = ['№ контакта', 'Имя контакта', 'Номер контакта']
        for contact in contacts:
            table.add_row(contact)
        print(table)


def add_contact(contacts: list) -> None:
    contact_name = input('Введите имя контакта: ')
    contact_phone = input('Введите номер контакта: ')
    contact_id = str(len(contacts) + 1)
    contacts.append([contact_id, contact_name, contact_phone])
    save_contacts(contacts)


def edit_contact(contacts: list) -> None:
    display_contacts(contacts)
    try:
        contact_id = int(input(
            'Введите номер контакта,'
            'который хотите редактировать: '
        ))
        if 1 <= contact_id <= len(contacts):
            contact = contacts[contact_id - 1]
            print(f'{contact[1]} - текущее имя контакта.')
            new_name = input(
                'Введите новое имя контакта. '
                'Нажмите Enter, если хотите оставить без изменений: ')
            if new_name:
                contact[1] = new_name
            print(f'{contact[2]} - текущий номер контакта.')
            new_phone = input(
                'Введите новый номер контакта. '
                'Нажмите Enter, если хотите оставить без изменений: ')
            if new_phone:
                contact[2] = new_phone
            save_contacts(contacts)
        else:
            print('Такого номера нет в списке.')
    except ValueError:
        print('Вы ввели не число.')


def delete_contact(contacts: list) -> None:
    display_contacts(contacts)
    try:
        contact_id = int(input(
            'Введите номер контакта, '
            'который хотите удалить: '
        ))
        if 1 <= contact_id <= len(contacts):
            contacts.pop(contact_id - 1)
            for i, contact in enumerate(contacts, start=1):
                contact[0] = str(i)
            save_contacts(contacts)
        else:
            print('Такого номера нет в списке.')
    except ValueError:
        print('Вы ввели не число.')


def main() -> None:
    print('Консольный помощник телефонных контактов.')
    contacts = load_contacts()
    while True:
        choice = print_menu()
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print('Программа завершает работу.\nДо свидания.')
            break
        else:
            print(
                f'Варианта "{choice}" '
                'не предусмотрено. Повторите попытку.\n'
            )


if __name__ == '__main__':
    main()
