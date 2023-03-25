from flask import Flask, request, redirect, render_template

from Controller.customer import get_customers, add_customer

app = Flask(__name__, template_folder='../templates/')


@app.route('/')
def index():
    users = get_customers()
    return render_template("home.html", users=users)


@app.route('/add_customer', methods=['POST'])
def add():
    # get the data from the request object
    name = request.form['name']
    phone_number = request.form['phone']
    address = request.form['address']

    add_customer(name, phone_number, address)
    return redirect('/')
