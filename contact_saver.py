import mysql.connector
import re
 
# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chinni@1901",   # change here
        database="contact_saver"
    )
 
# ---------- Validations ----------
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10
 
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
 
# ---------- Add Contact ----------
def add_contact():
    try:
        conn = get_connection()
        cursor = conn.cursor()
 
        name = input("Enter Name: ")
        phone = input("Enter Phone (10 digits): ")
 
        if not is_valid_phone(phone):
            print("❌ Invalid phone number!")
            return
 
        email = input("Enter Email: ")
        if not is_valid_email(email):
            print("❌ Invalid email format!")
            return
 
        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, phone, email))
        conn.commit()
        print("✅ Contact added successfully!")
 
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
 
# ---------- View Contacts ----------
def view_contacts():
    try:
        conn = get_connection()
        cursor = conn.cursor()
 
        cursor.execute("SELECT * FROM contacts")
        records = cursor.fetchall()
 
        print("\n--- Contact List ---")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
 
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
 
# ---------- Search Contact ----------
def search_contact():
    try:
        conn = get_connection()
        cursor = conn.cursor()
 
        key = input("Enter Name or Phone to search: ")
        query = "SELECT * FROM contacts WHERE name=%s OR phone=%s"
        cursor.execute(query, (key, key))
        records = cursor.fetchall()
 
        if records:
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
        else:
            print("No contact found.")
 
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
 
# ---------- Update Contact ----------
def update_contact():
    try:
        conn = get_connection()
        cursor = conn.cursor()
 
        cid = input("Enter Contact ID to update: ")
 
        name = input("Enter New Name: ")
        phone = input("Enter New Phone: ")
        email = input("Enter New Email: ")
 
        query = "UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s"
        cursor.execute(query, (name, phone, email, cid))
        conn.commit()
 
        if cursor.rowcount > 0:
            print("✅ Contact updated successfully!")
        else:
            print("❌ Contact ID not found.")
 
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
 
# ---------- Delete Contact ----------
def delete_contact():
    try:
        conn = get_connection()
        cursor = conn.cursor()
 
        cid = input("Enter Contact ID to delete: ")
        cursor.execute("DELETE FROM contacts WHERE id=%s", (cid,))
        conn.commit()
 
        if cursor.rowcount > 0:
            print("✅ Contact deleted successfully!")
        else:
            print("❌ Contact ID not found.")
 
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
 
# ---------- Menu ----------
def menu():
    while True:
        print("\n===== Contact Saver Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
 
        choice = input("Enter your choice: ")
 
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
            print("Exiting application...")
            break
        else:
            print("Invalid choice!")
 
# ---------- Run ----------
if __name__ == "__main__":
    menu()
 