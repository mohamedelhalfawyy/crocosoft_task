import mysql.connector


def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="crocosoftCR"
    )

    return db
