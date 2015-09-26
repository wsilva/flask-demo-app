# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, g
import sqlite3
import socket


DATABASE = './database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def main():

    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)

    query = query_db('select count(*) as qtde from subscription')

    subscriptions=query[0]['qtde']
    return render_template('index.html', subscriptions=subscriptions, ipaddr=ipaddr, hostname=hostname)

@app.route("/subscribe", methods=['POST','GET'])
def subscribe():

    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)

    _email = request.form['inputEmail']
    if _email :
        g.db.execute('insert into subscription (email) values (?)', [_email])
        g.db.commit()
        return render_template("subscribed.html", email=_email, ipaddr=ipaddr, hostname=hostname)

    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)