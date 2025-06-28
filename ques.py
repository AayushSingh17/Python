import sqlite3
conn = sqlite3.connect("emp_records.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp_records(
        Id INTEGER PRIMARY KEY,
        Name TEXT,
        Department TEXt,
        Salary TEXT )
                """)

emp_data = [
    ("Aayu", "IT", 150000),
    ("Aditya", "IT", 145000),
    ("Jay", "IT", 140000),
    ("Aman", "IT", 140000),
    ("Rocky", "IT", 80000),
    ("Salmon", "IT", 85000)
]
cursor.executemany("""
        INSERT INTO emp_records(NAME,DEPARTMENT,SALARY)
                            VALUES(?,?,?)

""",emp_data)
conn.commit()
