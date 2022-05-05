# Importing a library
import sqlite3

# Using a function for connection to the database
def connect():

    # Connecting to the database
    conn = sqlite3.connect("Paramjeet.db")

    cursor = conn.cursor()

    table = """INSERT INTO Paramjeet_851 (StudentID, StudentFirstName, StudentLastName, City) VALUES (835851, 'Paramjeet', 'Randhawa', 'Mississauga')"""

    updateDB = "UPDATE Paramjeet_851 SET City = 'Toronto' WHERE StudentID = 835851"

    # cursor.execute("SELECT * FROM Paramjeet_851")

    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    cursor.execute("DELETE FROM Paramjeet_851 WHERE StudentID = 835851")

    conn.commit()

    conn.close()


# This is the main function
if __name__ == '__main__':
    # Calling the function
    connect()


