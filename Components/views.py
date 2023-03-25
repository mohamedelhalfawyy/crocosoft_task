from flask import Flask, request, redirect, render_template

from Controller.customer import get_customers, add_customer, update_customer

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


@app.route('/update')
def customer():
    customer_id = request.args.get('customer_id')
    return render_template('update_customer.html', customer_id=customer_id)


# function to update a contact in the database
@app.route("/update_customer", methods=["POST"])
def update():
    customer_id = request.form["customer_id"]
    name = request.form["name"]
    phone = request.form["phone"]
    address = request.form["address"]

    update_customer(customer_id, name, phone, address)
    return redirect("/")
