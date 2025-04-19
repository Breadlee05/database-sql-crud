 Add new student records
- View all students
- Search for a student by roll number
- Update student details
- Delete student records

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

## Setup Instructions

1. **Install MySQL Server** if not already installed. Create a database named `student_db`.

2. **Create the students table** by running the SQL script provided in `database.sql`:

```sql
-- database.sql
CREATE TABLE students (
    roll_number INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100)
);
```

You can execute this script using MySQL command line or any MySQL client.

3. **Install Python dependencies**:

```bash
pip install mysql-connector-python
```

## Usage

Run the Python script `curd.py`:

```bash
python curd.py
```

You will see a menu with options to add, view, search, update, or delete student records. Follow the prompts to perform operations.

## Notes

- Ensure MySQL server is running and accessible with the credentials specified in the script (`host='localhost'`, `user='root'`, `password='avenger@54321'`).
- Modify the connection parameters in `curd.py` if your MySQL setup differs.

## License

This project is provided as-is without any warranty.
