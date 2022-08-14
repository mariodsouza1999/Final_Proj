from flask import Flask
from flask import render_template
import socket
import mysql.connector
import os

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"
Dg_image = os.environ.get('bg_image') or "no image"
NAME =  os.environ.get('NAME')

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', color=color, Dg_image=Dg_image, NAME=NAME)

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
