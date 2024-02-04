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
def student_login():
    if request.method == 'POST':
        uname = request.form.get("id")
        passwd = request.form.get("password")
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, password FROM student_details WHERE id = %s", [uname])
        user = cur.fetchone()
        cur.close()

        if user and user[1] == passwd:
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", logintry="Login Failure")
    else:
        return render_template("login.html")
    

@app.route('/dashboard')
def dashboard():
    return render_template('dashstudent.html')

@app.route('/student_mart')
def student_mart():
    return render_template('smart.html')

@app.route('/general_stores')
def general_stores():
    return render_template('gstores.html')

@app.route('/canteens')
def canteens():
    return render_template('canteen.html')

@app.route('/vendor_login', methods = ['POST'])
def vendor_login():
    if request.method == 'POST':
        uname = request.form.get("id")
        passwd = request.form.get("password")
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, password FROM vendor_details WHERE id = %s", [uname])
        user = cur.fetchone()
        cur.close()

        if user and user[1] == passwd:
            return redirect(url_for('vendor_dashboard'))
        else:
            return render_template("login.html", logintry="Login Failure")
    else:
        return render_template("login.html")

@app.route('/vendor_dashboard')
def vendor_dashboard():
    return render_template('dashvendor.html')

@app.route('/inventory')
def inventory():
    return render_template('vendorinventory.html')

@app.route('/wishlist')
def wishlist():
    return render_template('vendorwishl.html')

# @app.route('/update_inventory', methods=['POST'])
# def update_inventory():
#     if request.method == 'POST':
#         # Loop through the form fields
#         for item_name, quantity in request.form.items():
#             # if item_name.startswith('quantity_'):  # This assumes your input names are like 'quantity_itemID'
#             # item_id = item_name.split('_')[1]  # Extract the item ID
            
#             # Update the database
#             cur = mysql.connection.cursor()
#             cur.execute("UPDATE shop_items SET quantity = %s WHERE name = %s;", (quantity, item_name))
#             mysql.connection.commit()
#             cur.close()

#         # Redirect to the inventory page or wherever you'd like
#         return redirect(url_for('inventory'))
@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    cur = mysql.connection.cursor()
    try:
        # Loop through the form fields
        for item_name, quantity in request.form.items():
            cur.execute("UPDATE shop_items SET quantity = %s WHERE name = %s;", (quantity, item_name))
        
        mysql.connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error or handle it as needed
    finally:
        cur.close()

    # Redirect to the inventory page or wherever you'd like
    return redirect(url_for('inventory'))


if __name__ == "__main__":
    app.run(debug=True,port=8000)