from Database.connectDatabase import connect_to_database

db = connect_to_database()

# create a cursor object
cursor = db.cursor()


# function to get all contacts from database
def get_customers():
    cursor.execute("SELECT * FROM customer")
    users = cursor.fetchall()
    return users


# function to add a new contact to the database
def add_customer(name, phone, address):
    # execute the SQL INSERT statement
    sql = "INSERT INTO customer (Name, Phone_Number, Address) VALUES (%s, %s, %s)"
    val = (name, phone, address)
    cursor.execute(sql, val)
    db.commit()
