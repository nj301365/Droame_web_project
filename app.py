from flask import Flask, redirect, render_template, request, url_for, flash,get_flashed_messages
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nikhil098@'
app.config['MYSQL_DB'] = 'operator'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', customers = data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Booking Added Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        location = request.form['location']
        drone = request.form['drone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers (customer_name, email, phone_number, location_id, drone_shot_id) VALUES (%s,%s,%s,%s,%s)", (name, email, phone, location, drone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['GET'])
def delete(id):
    flash("Boooking has been deleted")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE id=%s", (id))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update/', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        location = request.form['location']
        drone = request.form['drone']
        # ttime = request.form['ttime']
        
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE customers         
        SET name=%s, email=%s, phone=%s, location=%s, drone=%s
        WHERE id=%s
        """,(name, email, phone, location, drone, id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))
        


if __name__ == "__main__":
    app.run(debug=True)

