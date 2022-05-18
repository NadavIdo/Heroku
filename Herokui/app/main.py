import json
from pydoc import render_doc
from flask import Flask
import sqlite3

app = Flask(__name__)

con = sqlite3.connect('example.db',check_same_thread=False)
cur = con.cursor()
def initdb():
    # Create table
    cur.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    # con.close()


@app.route("/")
def home_view():
		return "<h1>Welcome to Geeks for Geeks</h1>"

@app.route("/test")
def test():
		return render_doc

@app.route("/about")
def about():
    res = []
    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        res.append( row)
    return json.dumps(res)
# uncomment to test localy
# if __name__ == "__main__":
# 		app.run()
