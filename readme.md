# Contact Management System

This is a simple contact management system implemented in Python. The program allows you to add, delete, edit, and view contacts. Each contact consists of a name and a phone number.

## Features

- **Add Contact**: Add a new contact by entering the name and phone number.
- **Delete Contact**: Delete a contact by entering the name.
- **Edit Contact**: Edit an existing contact's name and/or phone number.
- **Show All Contacts**: Display all the contacts that have been added.

## How to Use

1. **Run the Program**:
   - Run the Python script. You will be presented with a menu of options.

2. **Menu Options**:
   - **1 - Add new Contact**: Enter the name and phone number to add a new contact.
   - **2 - Delete a Contact**: Enter the name of the contact you want to delete.
   - **3 - Edit Contact**: Enter the name of the contact you want to edit, then update the name and/or phone number.
   - **4 - Show all Contacts**: Display a list of all contacts.
   - **X - Exit**: Exit the program.

## Example

```python
Enter your choice: 1
Enter contact name: Alice
Enter contact phone number: 123456789
Contact Alice added.

Enter your choice: 4
All contacts:
Alice - 123456789

Enter your choice: 3
Enter the name of the contact to edit: Alice
Enter new name (or press Enter to keep Alice): Alicia
Enter new phone number (or press Enter to keep 123456789): 987654321
Contact Alice updated.

Enter your choice: 4
All contacts:
Alicia - 987654321

Enter your choice: X
Bye Bye