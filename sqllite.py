import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        Id INTEGER PRIMARY KEY,
        Name TEXT,
        Age INTEGER,
        Grade TEXT )
                """)


conn.commit()

# cursor.execute("""
#     INSERT INTO student(name, age, grade)
#                 VALUES(?,?,?)
#                 """,('Aayush', '15', 'A++'))
# conn.commit()

# student_data = [
#     ("Aayu", 10, "A+"),
#     ("Aditya", 20, "A"),
#     ("Jay", 14, "B+"),
#     ("Aman", 16, "B"),
#     ("Rocky", 19, "C+"),
#     ("Salmon", 21, "C")
# ]
# cursor.executemany("""
#         INSERT INTO student(name,age,grade)
#                             VALUES(?,?,?)

# """,student_data)
# conn.commit()

cursor.execute("""
        SELECT * FROM student
               """)

rows = cursor.fetchall()
# # rows = cursor.fetchone()
# # rows = cursor.fetchmany()

for row in rows :
    print(row)


# cursor.execute("""
#     UPDATE student
#     SET grade = ?
#     WHERE name = ?
# """,("B+", "Salmon"))

# conn.commit()

# cursor.execute("""
#     DELETE FROM student
#         WHERE name = ?
#                 """,("Rocky",))
# conn.commit()

name = input("Enter the name to delete data:")
cursor.execute("""
     DELETE FROM student
         WHERE name = ?
                 """,(name,))
conn.commit()

cursor.execute("""
        SELECT * FROM student
               """)

rows = cursor.fetchall()
for row in rows :
    print(row)

cursor.execute("""
    SELECT * FROM students
                """)

rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

