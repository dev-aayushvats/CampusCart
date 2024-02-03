from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'campuscart'
mysql = MySQL(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
#     cur = mysql.connection.cursor()
#     cur.execute("select name from student_details")
    # ans = cur.fetchone()
    # cur.close()
    # return render_template('login.html',name=ans)
    # if request.method == 'POST':
    #     userDetails = request.form
    #     id = userDetails("id")
    #     name = userDetails("name")
    #     email = userDetails['email']
    #     password = userDetails['password']
        
    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO users(id, name, email, password) VALUES(%s, %s, %s, %s)", (id, name, email, password))
    #     mysql.connection.commit()
    #     print(cur.execute("select * from student_details"))
    #     cur.close()
    #     return 'Registration successful'
    return render_template('login.html')
@app.route('/student_login', methods = ['POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get("id")
        passwd = request.form.get("password")
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, password FROM student_details WHERE id = %s", [uname])
        user = cur.fetchone()
        cur.close()

        if user and user[1] == passwd:
            return render_template("dashstudent.html")
        else:
            return render_template("login.html", logintry="Login Failure")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)