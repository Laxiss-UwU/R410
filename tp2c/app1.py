from fastapi import FastAPI
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
   	 user="root",
   	 password="foo",
   	 database="TP2C")

app = FastAPI()

@app.get("/lieux")
def get_lieu():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM lieux")
	lieux = cursor.fetchall()
	cursor.close()
	return {"lieu" :lieux}
