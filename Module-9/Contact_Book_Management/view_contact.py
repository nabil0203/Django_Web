from read_write_contact import read_contact

def view_contact():
    contacts = read_contact()
    if not contacts:
        print("No contacts found.")
        return
    
    filtered_contacts = [
        c for c in contacts
        if not all(k == c[k] for k in ["name", "phone", "email", "address"])
    ]
    if not filtered_contacts:
        print("No valid contact entries found.")
        return
    
    print("\nAll Contacts:\n")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. Name : {c['name']}")
        print(f"   Phone : {c['phone']}")
        print(f"   Email : {c['email']}")
        print(f"   Address: {c['address']}\n")