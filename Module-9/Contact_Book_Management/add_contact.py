from read_write_contact import read_contact
from read_write_contact import write_contact


def get_valid_phone():
    while 1:
        phone = input("Enter Phone Number: ").strip()
        if phone.isdigit() and len(phone) == 11:
            return phone
        else:
            print("Invalid phone number. It must be exactly 11 digits.")


def add_contact():
    name = input("Enter Name: ")
    phone = get_valid_phone()
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = read_contact()

    if any(c['phone'] == phone for c in contacts):
        print("Error: Phone number already exists for another contact.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    write_contact(contacts)
    print("Contact added successfully!")