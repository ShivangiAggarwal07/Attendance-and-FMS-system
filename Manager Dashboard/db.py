import sqlite3 as sql

# Connect to SQLite database
con = sql.connect('db_web.db')
cur = con.cursor()

# Drop tables if they already exist
cur.execute("DROP TABLE IF EXISTS tasks")
cur.execute("DROP TABLE IF EXISTS attendance")
cur.execute("DROP TABLE IF EXISTS employees")

# Create employees table
cur.execute('''CREATE TABLE employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL)''')

# Insert sample employees
employees = [
    ('John Doe',),
    ('Jane Smith',),
    ('Michael Brown',),
    ('Emily Davis',)
]

cur.executemany('INSERT INTO employees (name) VALUES (?)', employees)

# Create tasks table with employee_id foreign key and status column
cur.execute('''CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                deadline TEXT NOT NULL,
                status TEXT,
                employee_id TEXT NOT NULL,
                team_lead INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees(id),
                FOREIGN KEY (team_lead) REFERENCES employees(id))''')


# Create attendance table
cur.execute('''CREATE TABLE attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                employee_id INTEGER,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                total_hours TEXT,
                punch_in TEXT,
                punch_out TEXT,
                FOREIGN KEY (employee_id) REFERENCES employees(id))''')

# Generate random attendance records with employee_id
attendance_records = [
    (1, '2024-06-01', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (2, '2024-06-01', 'Present', '7.5 hours', '08:30 AM', '04:00 PM'),
    (3, '2024-06-01', 'Absent', '', '', ''),
    (4, '2024-06-01', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (1, '2024-05-31', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (2, '2024-05-31', 'Present', '7.5 hours', '08:30 AM', '04:00 PM'),
    (3, '2024-05-31', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (4, '2024-05-31', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (1, '2024-05-30', 'Absent', '', '', ''),
    (2, '2024-05-30', 'Present', '7 hours', '09:00 AM', '04:00 PM'),
    (3, '2024-05-30', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (4, '2024-05-30', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (1, '2024-05-29', 'Present', '8 hours', '08:00 AM', '04:00 PM'),
    (2, '2024-05-29', 'Present', '7.5 hours', '08:30 AM', '04:00 PM'),
    (3, '2024-05-29', 'Absent', '', '', ''),
    (4, '2024-05-29', 'Present', '8 hours', '08:00 AM', '04:00 PM')
]

# Insert records into the attendance table
for record in attendance_records:
    employee_id = record[0]
    cur.execute('SELECT name FROM employees WHERE id = ?', (employee_id,))
    employee_name = cur.fetchone()[0]
    attendance_record_with_name = (employee_name,) + record
    cur.execute('''INSERT INTO attendance 
                   (employee_name, employee_id, date, status, total_hours, punch_in, punch_out) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)''', attendance_record_with_name)

# Insert sample tasks with status
tasks = [
    ('Complete project report', '2024-06-10', 'Completed',1),
    ('Prepare presentation', '2024-06-12', 'Ongoing', 2),
    ('Update website', '2024-06-15', 'Not Started', 3),
    ('Organize meeting', '2024-06-11', 'Ongoing', 4),
    ('Design new logo', '2024-06-13', 'Completed', 1),
    ('Test new software', '2024-06-14', 'Not Started', 2),
    ('Conduct survey', '2024-06-16', 'Ongoing', 3),
    ('Prepare budget report', '2024-06-17', 'Not Started', 4)
]

cur.executemany('''INSERT INTO tasks (description, deadline, status, employee_id) 
                   VALUES (?, ?, ?, ?)''', tasks)

# Commit changes and close connection
con.commit()
con.close()
