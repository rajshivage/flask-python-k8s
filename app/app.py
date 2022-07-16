"""
APIs to Create, Read, Update, Delete authors using Flask Python Framework

"""
import os
from flask import jsonify, request, Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)


@app.route("/")
def index():
    """
    Function to test the functionality of the API
    """
    return "Hello, world!"


@app.route("/authors", methods=["POST"])
def add_author():
    """
    Function to add a authors to the MySQL database
    """
    req = request.json
    name = req["name"]
    email = req["email"]
    book = req["book"]
    publication = req["publication"]
    description = req["description"]

    if name and email and book and publication and request.method == "POST":
        sql = "INSERT INTO authors(name, email, book, publication, description) " \
              "VALUES(%s, %s, %s)"
        data = (name, email, book, publication, description)
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
            resp = jsonify("Author added successfully!")
            resp.status_code = 200
            return resp
        except Exception as exception:
            return jsonify(str(exception))
    else:
        return jsonify("Please provide name, email, book and publication")

@app.route("/authors")
def get_authors():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM authors"
    cursor.execute(sql)
    records = cursor.fetchall()
    cursor.close()
    resp = jsonify(records)
    return resp
      
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)