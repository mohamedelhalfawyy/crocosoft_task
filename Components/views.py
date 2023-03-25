from flask import Flask, request, redirect, render_template
from Database.connectDatabase import connect_to_database

app = Flask(__name__, template_folder='../templates/')

db = connect_to_database()

# create a cursor object
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('add_customer.html')


@app.route('/add_customer', methods=['POST'])
def add_customer():
    # get the data from the request object
    name = request.form['name']
    phone_number = request.form['phone']
    address = request.form['address']

    # execute the SQL INSERT statement
    sql = "INSERT INTO customer (Name, Phone_Number, Address) VALUES (%s, %s, %s)"
    val = (name, phone_number, address)
    cursor.execute(sql, val)
    db.commit()

    return redirect('/')
