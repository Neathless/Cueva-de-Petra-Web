from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('menu'))

@app.route('/inventario')
def inventario():
    return render_template('alta_inventario.html')

@app.route('/menu')
def menu():
    return render_template('menu_cafeteria.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
