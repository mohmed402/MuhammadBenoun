import sqlite3
import sqlite3 as db

connection = db.connect("BouncyCastle.db")
cursor = connection.cursor()


if connection is not None:
    print("connected to database")
else:
    print("cannot connect")


query = """
CREATE TABLE IF NOT EXISTS 'Person' (
    'Person_ID'             INTEGER,
    'FirstName'             TEXT,
    'LastName'              TEXT,
    'Email'                 TEXT,
    'HouseNumber'           INTEGER,
    'PostCode'              TEXT,
    'PhoneNumber'           INTEGER,
    'PersonType_ID'         INTEGER,
    PRIMARY KEY('Person_ID' AUTOINCREMENT)    
    FOREIGN KEY (PersonType_ID) REFERENCES PersonType(PersonType_ID) ON UPDATE RESTRICT ON DELETE RESTRICT
)
"""


query1 = """
CREATE TABLE IF NOT EXISTS 'BouncyCastle' (
    'BouncyCastle_ID'       INTEGER,
    'Name'                  TEXT,
    'Size'                  TEXT,
    'Colour_ID'             TEXT,
    'CapacityLimit'         INTEGER,
    'HireCost'              REAL,
    'Availability_ID'       INTEGER,
    PRIMARY KEY('BouncyCastle_ID' AUTOINCREMENT),
    FOREIGN KEY (Availability_ID) REFERENCES InStock(Availability_ID) ON UPDATE CASCADE,
    FOREIGN KEY (Colour_ID) REFERENCES Colour(Colour_ID) ON UPDATE CASCADE

)
"""

# insert_query = "INSERT INTO course (CourseName, CourseValidator) VALUES (?, ?)"
# val = ("SoftDEV", 'MMU')
# cursor.execute(insert_query, val)


query2 = """
CREATE TABLE IF NOT EXISTS 'Booking' (
    'Booking_ID'           INTEGER,
    'Person_ID'            INTEGER,
    'BookingDate'          DATE,
    'ReturnDate'           DATE,
    'AmountToBePaid'       REAL,
    'PaymentType_ID'       INTEGER,
    'employee_ID'          INTEGER,
    'BouncyCastle_ID'      INTEGER,
    PRIMARY KEY ('Booking_ID' AUTOINCREMENT), 
    FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (employee_ID) REFERENCES Person(Person_ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (PaymentType_ID) REFERENCES PaymentType(PaymentType_ID) ON UPDATE CASCADE,
    FOREIGN KEY (BouncyCastle_ID) REFERENCES BouncyCastle(BouncyCastle_ID) ON UPDATE CASCADE

)
"""

query3 = """
CREATE TABLE IF NOT EXISTS 'InStock' (
    'Availability_ID'       INTEGER,
    'Availability'          TEXT,
    PRIMARY KEY ('Availability_ID' AUTOINCREMENT)
)

"""
query4 = """
CREATE TABLE IF NOT EXISTS 'PersonType' (
    'PersonType_ID'         INTEGER,
    'Type'                  TEXT,
    PRIMARY KEY ('PersonType_ID' AUTOINCREMENT)
)
"""
query5 = """
CREATE TABLE IF NOT EXISTS 'PaymentType' (
    'PaymentType_ID'        INTEGER,
    'Type'                  TEXT,
    PRIMARY KEY ('PaymentType_ID' AUTOINCREMENT)
)
"""

query6 = """
CREATE TABLE IF NOT EXISTS 'Colour' (
    'Colour_ID'       INTEGER,
    'Colour'          TEXT,
    PRIMARY KEY ('Colour_ID' AUTOINCREMENT)
)"""


def add_data_to_table(table, person_ID, booking_date, return_date, amount_to_be_paid, payment_type_ID, employee_ID, bouncy_castle_ID):
    connection = sqlite3.connect("BouncyCastle.db")
    cursor = connection.cursor()
    if table == "1":
        query = "INSERT INTO Booking(Person_ID, BookingDate, ReturnDate, AmountToBePaid, PaymentType_ID, BouncyCastle_ID) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (person_ID, booking_date, return_date,
                       amount_to_be_paid, payment_type_ID, employee_ID, bouncy_castle_ID))
        connection.commit()
        connection.close()

    if connection is not None:
        print("Added to database")


def update_data_in_table(table_name, field_to_update, new_value, row_id):
    connection = db.connect("BouncyCastle.db")
    cursor = connection.cursor()
    query = f"UPDATE {table_name} SET {field_to_update} = ? WHERE {table_name}_id = ?"
    cursor.execute(query, (new_value, row_id))
    connection.commit()
    connection.close()
    if connection is not None:
        print("updated in database")


def delete_data_from_table(id, table):
    connection = sqlite3.connect("BouncyCastle.db")
    cursor = connection.cursor()
    if table == "1":
        table = "Booking"
    query = f"DELETE FROM {table} WHERE {id} = ?"
    cursor.execute(query, (id,))
    connection.commit()
    connection.close()
    if connection is not None:
        print("deleted in database")


def rename_field_in_table(old_name, new_name):
    connection = db.connect("BouncyCastle.db")
    cursor = connection.cursor()
    query = f"ALTER TABLE home RENAME COLUMN {old_name} TO {new_name}"
    cursor.execute(query)
    connection.commit()
    connection.close()
    if connection is not None:
        print("updated field name in database")


queryy = "SELECT BouncyCastle_ID, name, CapacityLimit, HireCost, InStock.Availability FROM BouncyCastle JOIN InStock USING(Availability_ID)"
cursor.execute(queryy)

# fetch all the rows returned by the query
rows = cursor.fetchall()


while True:
    action = input(
        "What would you like to do (add data (1) - update data (2) - delete data(3) - rename field(4) - info about bouncy Castles  (5) or x to exit): ")
    if action == "1":
        table = input(
            "What would you like to add (Booking(1) -- Person(2) -- Return (r)): ")
        while True:
            if table == "1":
                print("Press 'r' to return")
                person_ID = input("Customer ID: ")
                if person_ID == "r":
                    break
                booking_date = input("Booking Date: ")
                return_date = input("Return Date: ")
                amount_to_be_paid = float(input("Amount To Be Paid: "))
                payment_type_ID = int(input("PaymentType-ID: "))
                employee_ID = int(input("employee-ID: "))
                bouncy_castle_ID = int(input("BouncyCastle-ID: "))
                add_data_to_table(table, person_ID, booking_date, return_date,
                                  amount_to_be_paid, payment_type_ID, employee_ID, bouncy_castle_ID)
            elif table == "r":
                break
    elif action == "2":
        table = int(input(
            "which table would you like to update (Booking(1) -- Person(2): "))
        field_to_update = input("which field would you like to update: ")
        new_value = input("new value: ")
        row_id = int(input("row id: "))
        table_name = ""
        if table == 1:
            table_name = "Booking"
        elif table == 2:
            table_name = "Person"
        # Add similar code for other tables
        update_data_in_table(table_name, field_to_update,
                             new_value, row_id)
    elif action == "3":
        table = int(input(
            "which table would you like to delete data from (Booking(1) -- Person(2): "))

        id = int(input("row id: "))
        delete_data_from_table(table, id)

    elif action == "4":
        table = int(input(
            "which table would you like to rename a field in (Booking(1) -- Person(2): "))
        old_field_name = input("old field name: ")
        new_field_name = input("new field name: ")
        rename_field_in_table(table, old_field_name, new_field_name)

    elif action == "5":
        for row in rows:
            print(row)

    elif action == "x":
        break


# cursor.execute('''DROP TABLE BouncyCastle''')
# cursor.execute('''ALTER TABLE Booking ADD COLUMN columnname datatype''')
cursor.execute(query)
cursor.execute(query1)
# cursor.execute(query2)
# cursor.execute(query3)
# cursor.execute(query4)
cursor.execute(query6)
connection.commit()
connection.close()
