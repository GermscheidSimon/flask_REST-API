from flask import Flask, jsonify, request
import psycopg2
import calendar

import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def getHello():
    print('GET REQ')

    cal = calendar.month(2020, 12)
    print ("Here is the calendar:")
    print (cal)
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=bookstore")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    query = "SELECT * FROM library;"
    cur.execute(query)

    # Retrieve query results
    records =   cur.fetchall()
    print(records)
    return jsonify(records)

@app.route("/", methods=['POST'])
def postInfo():
    print('POST REQ')
    print(request.is_json)
    req = request.get_json()
    print(req)
    print(type(req))
    # insertData = ['test','testing','today']
    # conn = psycopg2.connect("dbname=bookstore")

    # # Open a cursor to perform database operations
    # cur = conn.cursor()
    # # Execute a query
    # query = "INSERT INTO library (title, author, published) VALUES (%s, %s, %s)"
    # cur.execute(query, insertData)

    # # Retrieve query results
    # records =   cur.fetchall()
    return 'ldkfjsljdfljs'

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
