

from flask import Flask, jsonify
import psycopg2
import json

app = Flask(__name__)



@app.route("/", methods=['GET'])
def getHello():
    print('GET REQ')
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=bookstore")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    query = "SELECT * FROM library;"
    cur.execute(query)

    # Retrieve query results
    records = cur.fetchall()
    print(records)
    return jsonify(records)

@app.route("/", methods=['POST'])
def postInfo():
    print('POST REQ')
    return 'post success'

@app.route("/", methods=['PUT'])
def putInfo():
    print('PUT REQ')
    return 'post success'

@app.route("/", methods=['DELETE'])
def deleteReq():
    print('delete request')
    return 'it\'s gone'

if __name__ == "__main__":
  app.run()
