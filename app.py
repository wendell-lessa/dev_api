from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0,
     'nome': 'Wendell',
     'habilidade': ['Python', 'Flask']},
    {'id': 1,
     'nome': 'Icaro',
     'habilidade': ['Anthem', 'Fortinite']},
    {'id': 2,
     'nome': 'teste1',
     'habilidades': ['java', 'php', 'jenkins']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Errosr', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o admin da API.'
            response = {'status': 'Error', 'mensagem': mensagem}
        return jsonify(response)
        # desenvolvedor = desenvolvedores[id]
        # print(desenvolvedor)
        # return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registor excluído'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        # posicao = len(desenvolvedores)
        dados['id'] = len(desenvolvedores)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Dados inseridos'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
