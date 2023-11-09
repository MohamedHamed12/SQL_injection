from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a sample SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Insert some sample data
# cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "password123"))
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/main')
def main():
    return render_template('search.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # This is a vulnerable query with user input directly embedded
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template('res.html', res="Success")
       
    else:
        return render_template('res.html', res="Failed")


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Search for products by name
    query = f"SELECT * FROM products WHERE name LIKE '{query}%'"
    cursor.execute(query)
    products = cursor.fetchall()
    conn.close()

    return render_template('search_results.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
