# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
from flask.ext.mysqldb import MySQL
import socket

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'demoapp'
app.config['MYSQL_HOST'] = 'db.inet'

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
# app.config['MYSQL_DATABASE_DB'] = 'demoapp'
# app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)


@app.route("/")
def main():

    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)

    cursor = mysql.connection.cursor()
    cursor.execute('select count(*) as qtde from subscription')
    query = cursor.fetchone()

    subscriptions="%s" % query
    return render_template('index.html', subscriptions=subscriptions, ipaddr=ipaddr, hostname=hostname)

@app.route("/subscribe", methods=['POST','GET'])
def subscribe():

    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)

    _email = request.form['inputEmail']
    if _email :
        cursor = mysql.connection.cursor()
        cursor.execute("insert into subscription (email) values ('{0}')".format(_email))
        mysql.connection.commit()
        return render_template("subscribed.html", email=_email, ipaddr=ipaddr, hostname=hostname)

    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)