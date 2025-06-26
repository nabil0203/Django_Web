import csv
import os

csv_contacts_file = "contacts.csv"

def ensure_file():
    if not os.path.exists(csv_contacts_file):
        with open(csv_contacts_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email", "address"])


# read contacts 
def read_contact():
    contacts = []
    try:
        with open(csv_contacts_file, "r") as file:
            for line in file:
                if line.strip():
                    name, phone, email, address = line.strip().split(",", 3)

                    if [name, phone, email, address] == ["name", "phone", "email", "address"]:
                        continue
                    address = address.strip('"')
                    contacts.append({
                        "name": name.strip('"'),
                        "phone": phone.strip('"'),
                        "email": email.strip('"'),
                        "address": address
                    })
    except FileNotFoundError:
        open(csv_contacts_file, "w").close()
    return contacts

# write contacts 
def write_contact(contacts):
    file_empty = not os.path.exists(csv_contacts_file) or os.stat(csv_contacts_file).st_size == 0

    with open(csv_contacts_file, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])

        if file_empty:
            writer.writeheader()
        writer.writerows(contacts)