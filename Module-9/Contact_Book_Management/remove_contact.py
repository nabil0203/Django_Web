from read_write_contact import read_contact
from read_write_contact import write_contact

def remove_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    contacts = read_contact()
    contact_to_delete = next((c for c in contacts if c['phone'] == phone), None)

    if not contact_to_delete:
        print("Contact not found.")
        return

    confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").lower()
    if confirm == "y":
        contacts = [c for c in contacts if c['phone'] != phone]
        write_contact(contacts)
        print("Contact deleted successfully!")
    else:
        print("Deletion cancelled.")