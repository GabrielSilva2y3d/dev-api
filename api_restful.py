from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills, SkillList

app = Flask(__name__)
api = Api(app)

dev = [

    {
        'id': '0',
        'nome': 'Gabriel',
        'habilidades': ['Python', 'flask', 'Django']
    }

]


# noinspection PyBroadException
class Dev(Resource):
    @staticmethod
    def get(id):
        try:
            response = dev[id]

        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe', format(id)
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response

    @staticmethod
    def put(id):
        dados = json.loads(request.data)
        dev[id] = dados
        return dados

    @staticmethod
    def delete(id):
        dev.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Registro Excluido'}


class ListaDevs(Resource):
    @staticmethod
    def post():
        dados = json.loads(request.data)
        posicao = len(dev)
        dados['id'] = posicao
        dev.append(dados)
        return {'status': 'Sucesso', 'mensagem': 'Registro inserido'}, dev[posicao]

    @staticmethod
    def get():
        return dev


api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(ListaDevs, '/dev')
api.add_resource(Skills, '/skills/<int:id>')
api.add_resource(SkillList,'/skills')
if __name__ == '__main__':
    app.run(debug=True)
