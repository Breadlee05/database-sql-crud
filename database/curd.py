import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='avenger@54321',  
            database='student_db'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None


def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        email = input("Enter Email: ")

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (roll_number, name, department, email) VALUES (%s, %s, %s, %s)",
                       (roll, name, dept, email))
        conn.commit()
        print("Student added successfully.")
        cursor.close()
        conn.close()
    except Error as e:
        print(" Failed to add student:", e)


def view_all_students():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        if not rows:
            print("No student records found.")
        else:
            print("\n-- All Students --")
            for row in rows:
                print(f"Roll: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Email: {row[3]}")
        
        cursor.close()
        conn.close()
    except Error as e:
        print(" Failed to retrieve students:", e)

def search_student():
    try:
        roll = int(input("Enter Roll Number to Search: "))
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE roll_number = %s", (roll,))
        row = cursor.fetchone()

        if row:
            print(f"\nFound:\nRoll: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Email: {row[3]}")
        else:
            print(" Student not found.")
        
        cursor.close()
        conn.close()
    except Error as e:
        print(" Error searching student:", e)

def update_student():
    try:
        roll = int(input("Enter Roll Number to Update: "))
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE roll_number = %s", (roll,))
        if cursor.fetchone() is None:
            print(" Student not found.")
            return

        name = input("Enter New Name: ")
        dept = input("Enter New Department: ")
        email = input("Enter New Email: ")
        cursor.execute(
            "UPDATE students SET name=%s, department=%s, email=%s WHERE roll_number=%s",
            (name, dept, email, roll)
        )
        conn.commit()
        print(" Student updated successfully.")
        cursor.close()
        conn.close()
    except Error as e:
        print(" Error updating student:", e)

def delete_student():
    try:
        roll = int(input("Enter Roll Number to Delete: "))
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE roll_number = %s", (roll,))
        conn.commit()

        if cursor.rowcount:
            print(" Student deleted.")
        else:
            print("Student not found.")
        
        cursor.close()
        conn.close()
    except Error as e:
        print(" Error deleting student:", e)

def main():
    while True:
        print("\n--- Student Records Menu ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
