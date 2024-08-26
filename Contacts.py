contacts = []

def menu():
    print("1 - Add new Contact")
    print("2 - Delete a Contact")
    print("3 - Edit Contact")
    print("4 - Show all Contacts")
    print("X - Exit")
    return input("Enter your choice: ").lower()  # להחזיר את הבחירה של המשתמש

def getUserData(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added.")

def DeleteContact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")  
    for contact in contacts:  
        if contact["name"].lower() == name_to_delete.lower():
            contacts.remove(contact)  
        print(f"Contact {name_to_delete} deleted.") 
        print(f"No contact found with the name {name_to_delete}.")

def EditContact(contacts):
    name_to_edit = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact["name"].lower() == name_to_edit.lower():
            new_name = input(f"Enter new name (or press Enter to keep {contact['name']}): ")
            new_phone = input(f"Enter new phone number (or press Enter to keep {contact['phone']}): ")
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            print(f"Contact {name_to_edit} updated.")
            return
    print(f"No contact found with the name {name_to_edit}.")

def showContacts(contacts):
    print("All contacts:")
    if contacts:
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']}")
    else:
        print("No contacts to show.")

while True:
    userSelection = menu()
    if userSelection == "x": 
        exit("Bye Bye")
    
    if userSelection == "1":
        getUserData(contacts)

    if userSelection == "2":     
        DeleteContact(contacts)  
    
    if userSelection == "3":
        EditContact(contacts)

    if userSelection == "4": 
        showContacts(contacts)


    

