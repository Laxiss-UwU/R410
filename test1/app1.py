from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route("/")
def home():
	return ("hello")

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "foo"
app.config["MYSQL_DB"] = "liste"
mysql = MySQL(app)

@app.route("/test")
def test():
	return ("test")

@app.route("/login", methods = ["POST", "GET"])
def login():
	if request.method == "GET":
		formulaire = render_template("forms.html")
		return formulaire

	if request.method == "POST":
		name = request.form["id"]
		age = request.form["name"]
		cursor = mysql.connection.cursor()
		cursor.execute(""" INSERT INTO liste VALUES(%s,%s)""",(id,name))
		mysql.connection.commit()
		cursor.close()
		return f"Done!!"
