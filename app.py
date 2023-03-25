from flask import Flask

from Database.connectDatabase import connect_to_database

app = Flask(__name__)

db = connect_to_database()


@app.route('/')
def index():  # put application's code here
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchall()
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
