from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote as url_quote


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Here you would add logic to verify the username and password
    if username == 'admin' and password == 'password':  # Example check
        return redirect(url_for('success'))
    return redirect(url_for('home'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
