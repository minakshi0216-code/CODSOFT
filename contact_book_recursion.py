#  Contact Book Program using recursion
# created by Minakshi
contacts = {}

def contact_book():
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exit")
        return  
    else:
        print("Invalid ")

    contact_book()

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully")

def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    search_name = input("Enter name to search: ")
    if search_name in contacts:
        info = contacts[search_name]
        print(f"\nName: {search_name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
    else:
        print("Contact not found")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
    
        phone = input("New phone: ") 
        email = input("New email: ") 
        address = input("New address: ") 

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' updated successfully")
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully")
    else:
        print("Contact not found")

contact_book()
