import view
import phone_book as p_b
import data_base as d_b


def main_menu(choice: int):
    if choice == 1:
        phone_book = p_b.get_phone_book()
        view.print_phone_book(phone_book)
    if choice == 2:
        d_b.load_data_base()
        view.load_book()
    if choice == 3:
        d_b.save_data_base()
        view.save_book()
    if choice == 4:
        contact = view.input_new_contact()
        p_b.add_contact(contact)
    if choice == 5:
        phone_book = p_b.get_phone_book()
        view.print_phone_book(phone_book)
        id = view.change_choice()
        try:
            if p_b.remove_contact(id):
                contact = view.input_new_contact()
                p_b.change_contact(id, contact)
                view.change_successful()
        except:
            view.change_error()
    if choice == 6:
        phone_book = p_b.get_phone_book()
        view.print_phone_book(phone_book)
        id = view.input_remove_contact()
        if p_b.remove_contact(id):
            view.remove_contact()
    if choice == 7:
        try:
            phone_book = p_b.get_phone_book()
            view.print_phone_book(phone_book)
            text = view.find_input()
            find_list = d_b.find_contact(phone_book, text)
            view.print_find_contact(find_list)
        except:
            view.find_error()
    if choice == 0:
        return True


def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break
