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


# function to update a contact in the database
def update_customer(customer_id, name, phone, address):
    query = "UPDATE customer SET Name = %s, Phone_Number = %s, Address = %s WHERE Customer_ID = %s"
    values = (name, phone, address, customer_id)
    cursor.execute(query, values)
    db.commit()


# function to delete a contact from the database
def delete_customer(customer_id):
    # Delete the contact from the database
    cursor.execute("DELETE FROM customer WHERE Customer_ID = %s", (customer_id,))
    db.commit()
