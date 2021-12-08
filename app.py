from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'nome':'Nelson',
        'habilidades':['Python', 'Django']
    },
    {
        'nome':'Arthur',
        'habilidades':['JavaScript', 'HTML']
    }
]

# Devolve um desenvolvedor pelo ID, tambem consegue alterar e deletar desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return  jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})

# Lista todos os desenvolvedores e permite registar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def listar_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro Inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)

