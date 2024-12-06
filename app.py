from password_generator import PasswordGenerator
from flask import Flask, render_template, request, redirect, flash, session
from forms import RegistrationForm, LoginForm
import sqlite3
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'architecture'  # Replace with a secure random string
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    if 'user' in session:
        return f"Hello, {session['user']}! <a href='/logout'>Logout</a>"
    return "Hello, Flask! <a href='/login'>Login</a> or <a href='/register'>Register</a>"

@app.route("/test")
def test():
    return "Test Route Works!"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        security_question = form.security_question.data

        # Save user to database
        try:
            connection = sqlite3.connect('mypass.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users (email, password, security_questions) VALUES (?, ?, ?)',
                           (email, password, security_question))
            connection.commit()
            connection.close()
            flash('Registration successful!', 'success')
            return redirect('/')
        except sqlite3.IntegrityError:
            flash('Email already exists. Please use a different one.', 'danger')

    return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check user credentials in the database
        connection = sqlite3.connect('mypass.db')
        cursor = connection.cursor()
        cursor.execute('SELECT password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        connection.close()

        if user and bcrypt.check_password_hash(user[0], password):
            session['user'] = email  # Store user's email in session
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('user', None)  # Remove user from session
    flash('Logged out successfully.', 'success')
    return redirect('/')

@app.route("/vault")
def vault():
    if 'user' not in session:
        flash('Please log in to view the vault.', 'danger')
        return redirect('/login')

    email = session['user']
    connection = sqlite3.connect('mypass.db')
    cursor = connection.cursor()

    # Get the logged-in user's ID
    cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    user_id = cursor.fetchone()[0]

    # Get all vault items for the user
    cursor.execute('SELECT id, name, username, password FROM vault WHERE user_id = ?', (user_id,))
    items = cursor.fetchall()
    connection.close()

    return render_template('vault.html', items=items)


@app.route("/vault/add", methods=["GET", "POST"])
def add_to_vault():
    if 'user' not in session:
        flash('Please log in to add items to the vault.', 'danger')
        return redirect('/login')

    if request.method == "POST":
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        email = session['user']
        connection = sqlite3.connect('mypass.db')
        cursor = connection.cursor()

        # Get the logged-in user's ID
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        user_id = cursor.fetchone()[0]

        # Insert the new item into the vault
        cursor.execute('INSERT INTO vault (user_id, name, username, password) VALUES (?, ?, ?, ?)',
                       (user_id, name, username, password))
        connection.commit()
        connection.close()

        flash('Item added to the vault!', 'success')
        return redirect('/vault')

    return render_template('add_vault.html')

@app.route("/vault/delete/<int:item_id>")
def delete_from_vault(item_id):
    if 'user' not in session:
        flash('Please log in to delete items from the vault.', 'danger')
        return redirect('/login')

    email = session['user']
    connection = sqlite3.connect('mypass.db')
    cursor = connection.cursor()

    # Get the logged-in user's ID
    cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    user_id = cursor.fetchone()[0]

    # Delete the item if it belongs to the logged-in user
    cursor.execute('DELETE FROM vault WHERE id = ? AND user_id = ?', (item_id, user_id))
    connection.commit()
    connection.close()

    flash('Item deleted successfully!', 'success')
    return redirect('/vault')

@app.route("/password-generator", methods=["GET", "POST"])
def password_generator():
    password = None
    if request.method == "POST":
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_numbers = 'numbers' in request.form
        use_special_chars = 'special' in request.form

        generator = PasswordGenerator()
        generator.set_length(length)
        generator.include_uppercase(use_uppercase)
        generator.include_numbers(use_numbers)
        generator.include_special_chars(use_special_chars)

        password = generator.generate()

    return render_template('password_generator.html', password=password)

import csv
from flask import Response

@app.route("/vault/export")
def export_vault():
    if 'user' not in session:
        flash('Please log in to export your vault.', 'danger')
        return redirect('/login')

    email = session['user']
    connection = sqlite3.connect('mypass.db')
    cursor = connection.cursor()

    # Get logged-in user's ID
    cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    user_id = cursor.fetchone()[0]

    # Get all vault items for the user
    cursor.execute('SELECT name, username, password FROM vault WHERE user_id = ?', (user_id,))
    items = cursor.fetchall()
    connection.close()

    # Generate CSV
    output = "Name,Username,Password\n"
    for item in items:
        output += f"{item[0]},{item[1]},{item[2]}\n"

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=vault_export.csv"}
    )

if __name__ == "__main__":
    app.run(debug=True)