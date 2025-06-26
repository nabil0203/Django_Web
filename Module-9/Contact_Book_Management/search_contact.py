from read_write_contact import read_contact

def search_contact():
    field = input("Search by 'name', 'email', or 'phone': ").strip().lower()
    valid_fields = ['name', 'email', 'phone']

    if field not in valid_fields:
        print("Invalid option. Please enter 'name', 'email', or 'phone'.")
        return

    query = input(f"Enter the {field}: ").strip().lower()
    contacts = read_contact()

    results = []
    for c in contacts:
        value = c[field].lower() if field != 'phone' else c[field]  
        if query in value:
            results.append(c)

    if results:
        print("\nSearch Result:\n")
        for c in results:
            print(f"Name : {c['name']}")
            print(f"Phone : {c['phone']}")
            print(f"Email : {c['email']}")
            print(f"Address: {c['address']}\n")
    else:
        print("No contact found.")