from flask import Flask,render_template
from flask_mysqldb import MySQL
from datetime import datetime
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Shad@1286'
app.config['MYSQL_DB']='flaskapp'

mysql = MySQL(app)

@app.route('/')
def home():
    cur=mysql.connection.cursor()
    cur.execute("select * from student")
    fetchdata=cur.fetchall()
    cur.close()
    return render_template("home.html",data=fetchdata)

if __name__=='__main__':
    app.run(debug=True)