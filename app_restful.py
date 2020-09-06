from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Errosr', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o admin da API.'
            response = {'status': 'Error', 'mensagem': mensagem}
        return response

    def put(self):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
