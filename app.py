import json
import mariadb
import dbcreds
import dbhelper

from flask import Flask
app = Flask(__name__)

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()




app.run(debug=True)
