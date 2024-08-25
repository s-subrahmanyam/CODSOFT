class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ").lower()
        results = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
        
        if results:
            for contact in results:
                self.display_contact(contact)
        else:
            print("No matching contact found.")

    def update_contact(self):
        search_term = input("Enter the name or phone number of the contact to update: ").lower()
        contact = next((contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone), None)
        
        if contact:
            self.display_contact(contact)
            name = input(f"Enter new name (leave blank to keep {contact.name}): ") or contact.name
            phone = input(f"Enter new phone number (leave blank to keep {contact.phone}): ") or contact.phone
            email = input(f"Enter new email (leave blank to keep {contact.email}): ") or contact.email
            address = input(f"Enter new address (leave blank to keep {contact.address}): ") or contact.address
            contact.update(name, phone, email, address)
            print(f"Contact for {name} updated successfully.")
        else:
            print("No matching contact found.")

    def delete_contact(self):
        search_term = input("Enter the name or phone number of the contact to delete: ").lower()
        contact = next((contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone), None)
        
        if contact:
            self.contacts.remove(contact)
            print(f"Contact for {contact.name} deleted successfully.")
        else:
            print("No matching contact found.")

    def display_contact(self, contact):
        print("\nContact Details:")
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

    def user_interface(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.user_interface()
