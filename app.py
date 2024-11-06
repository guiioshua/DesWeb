from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL


##  CONFIGURAÇÃO DO FLASK  ##
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'contatos'

##  CRIAÇÃO DO OBJETO DO FLASK  ##
# É possível agora aplicar métodos a mysql que estão relacionados à função MYSQL #
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('Home.html')

#  Define o método GET para abrir /Contato, POST para quando o botão de submit do dentro do HTML de Contato chamar POST  #
@app.route('/Contato', methods=['GET', 'POST']) 
def contato():
    if request.method == 'POST':
        #  Quando o método POST for requisitado através do chamamento do botão de input, o código abaixo rodará  #
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO message(email, topic, description) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
        #  Ao fim da postagem da mensagem no banco de dados, retorna um redirecionamento para a rota Mensagens  #
        return redirect('/Mensagens')  

    #  Se o request não for um POST, sai da condicional e vai pra cá, retornando a renderização da página Contato  #
    return render_template('contato.html') 

@app.route('/Mensagens')
def messages():
    #  Atribui a 'messages' as tabelas resultante da requisição SQL  #
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM message")
    messages = cur.fetchall()
    cur.close()

    # Renderiza a página Mensagens
    # Retorna uma variável chamada messages que pode ser chamada pelo nome de messages no código da página
    return render_template('Mensagens.html', messages=messages)

@app.route('/quemSomos')
def quemSomos():
    return render_template('quemSomos.html')

if __name__ == '__main__':
    app.run(debug=True)

