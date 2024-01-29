from flask import Flask,render_template
from flask_mysqldb import MySQLdb
from datetime import datetime
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB']='flaskapp'

db=MySQL(app)
@app.route('/')
    cur=mysql.connection.cursor()
    cur.execute("select * from student")
    fetchdata=cur.fetchall()
    cur.close()
    return render_template("index.html",data=fetchdata)

if __name__=='__main__':
    app.run(debug=True)
