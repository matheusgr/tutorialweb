from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, navigation=[{'href': '/', 'caption': 'home'}])

questoes = [{"nome" : "Exemplo", "texto": "Questão de exemplo"}]

@app.route('/questao', methods=['GET', 'POST','DELETE', 'PATCH'])
def question():
    if request.method == 'GET':
        start = request.args.get('id', default=-1, type=int)
        if start > len(questoes):
            return "Questao inexistente", 404
        return render_template('questao.html', questao=questoes[start])

    if request.method == 'POST':
        nome = request.form.get('nome')
        texto = request.form.get('texto')
        questoes.append({"nome": nome, "texto": texto})
        return render_template('questao.html', questao=questoes[-1])