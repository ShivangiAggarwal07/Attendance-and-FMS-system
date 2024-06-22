from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db_web.db')
    conn.row_factory = sqlite3.Row
    return conn
def fetch_absent_records():
    con = sqlite3.connect('db_web.db')
    cur = con.cursor()
    cur.execute("SELECT employee_name, employee_id, date, status FROM attendance WHERE status = 'Absent'")
    absent_records = cur.fetchall()
    con.close()
    return absent_records

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add_task', methods=['POST'])
def add_task():
    conn = get_db_connection()
    description = request.form['description']
    deadline = request.form['deadline']
    employee_id = request.form.getlist('employee_id')
    team_lead = request.form['team_lead']

    for eid in employee_id:
        conn.execute('INSERT INTO tasks (description, deadline, employee_id, team_lead) VALUES (?, ?, ?, ?)',
                     (description, deadline, eid, team_lead))
    
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()
    if request.method == 'POST':
        description = request.form['description']
        deadline = request.form['deadline']
        employee_id = request.form['employee[]']  # Get selected employee ID
        team_lead = request.form['team_lead']
        
        conn.execute('INSERT INTO tasks (description, deadline, employee_id,team_lead) VALUES (?, ?, ?,?)',
                     (description, deadline, employee_id,team_lead))
        conn.commit()
        return redirect(url_for('tasks'))
    
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    employees = conn.execute('SELECT * FROM employees').fetchall()  # Fetch employees
    conn.close()
    return render_template('tasks.html', tasks=tasks, employees=employees)

@app.route('/attendance')
def attendance():
    conn = get_db_connection()
    attendance_records = conn.execute('SELECT * FROM attendance').fetchall()
    conn.close()
    return render_template('attendance.html', attendance_records=attendance_records)
@app.route('/assigned-tasks')
def assigned_tasks():
    conn = get_db_connection()
    tasks = conn.execute('''
        SELECT tasks.id, tasks.description, tasks.deadline, employees.name AS employee_name, tasks.status 
        FROM tasks 
        JOIN employees ON tasks.employee_id = employees.id
    ''').fetchall()
    conn.close()
    return render_template('assigned.html', tasks=tasks)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))
# Route to display the ongoing tasks
@app.route('/ongoing')
def ongoing_tasks():
    conn = get_db_connection()
    ongoing_tasks = conn.execute("SELECT * FROM tasks WHERE status='Ongoing'").fetchall()
    conn.close()
    return render_template('ongoing.html', tasks=ongoing_tasks)
@app.route('/absent_report')
def absent_report():
    # Fetch the absent records from the database
    absent_records = fetch_absent_records()
    
    return render_template('absent_report.html', absent_records=absent_records)
@app.route('/attendence_reports')
def attendence_reports():
    # Fetch the absent records from the database
    conn = get_db_connection()
    attendance_records = conn.execute('SELECT * FROM attendance').fetchall()
    conn.close()
    return render_template('attendence_reports.html', attendance_reports=attendance_records)


if __name__ == '__main__':
    app.run(debug=True)
