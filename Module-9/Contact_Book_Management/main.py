from add_contact import add_contact
from view_contact import view_contact
from search_contact import search_contact
from remove_contact import remove_contact
from read_write_contact import ensure_file


ensure_file()


# Main Menu
print("Welcome to the Contact Book CLI System!")
print("Loading contacts from contacts.csv... Done!")

while True:
    print("=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        break
    else:
        print("Invalid Option!!")


print("Thank you for using the Contact Book CLI System. Goodbye!")

