from flask import send_from_directory
from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

questoes = [{"nome" : "Exemplo", "texto": "Questão de exemplo"}]

@app.route('/questao', methods=['GET', 'POST','DELETE', 'PATCH'])
def question():
    if request.method == 'GET':
        start = request.args.get('id', default=-1, type=int)
        if start > len(questoes):
            return "Questao inexistente", 404
        return jsonify(questoes[start])

    if request.method == 'POST':
        nome = request.form.get('nome')
        texto = request.form.get('texto')
        questoes.append({"nome": nome, "texto": texto})
        return jsonify(questao=questoes[-1])