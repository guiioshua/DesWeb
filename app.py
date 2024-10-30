from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contato'
mysql = MySQL(app)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Contato', methods=['POST','GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (email, assunto, descricao) VALUES (%s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
    return render_template('contato.html')

@app.route('/quemSomos')
def quemSomos():
    return render_template('quemSomos.html')

if __name__ == '__main__':
    app.run(debug=True)

