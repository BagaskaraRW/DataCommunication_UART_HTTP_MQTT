from flask import Flask, json, request
import sqlite3
import math

api = Flask(__name__)

@api.route('/komdat/fungames/6.1/data', methods=['GET'])
def get_data():
    DATABASE_FILE = 'pkd.db'
    db_conn = sqlite3.connect(DATABASE_FILE)
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM pkd ORDER BY id DESC LIMIT 1")
    data = cursor.fetchall()[0][2]
    pesan = {"status": 200,"data": data}
    return json.dumps(pesan)

if __name__ == '__main__':
    api.run(host="0.0.0.0")
