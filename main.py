from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'

app.config['MYSQL_USER']='root'

app.config['MYSQL_PASSWORD']= ''

app.config['MYSQL_DB']='flask_mysql'

mysql = MySQL(app)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        UserDetails = request.form
        name = UserDetails['name']
        email= UserDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) values (%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

