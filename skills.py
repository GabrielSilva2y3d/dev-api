from flask_restful import Resource
from flask import request
import json

skills_list = [
    {'id': '0',
     'skill': 'Python'},

    {'id': '1',
     'skill': 'Java'},

    {'id': '2',
     'skill': 'PHP'},

    {'id': '3',
     'skill': 'C#'},

    {'id': '4',
     'skill': 'Ruby'},

    {'id': '5',
     'skill': 'JavaScript'},

    {'id': '6',
     'skill': 'Unity'}

]


class Skills(Resource):
    @staticmethod
    def get(id):
        try:
            response = skills_list[id]

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
        skills_list[id] = dados
        return dados

    @staticmethod
    def delete(id):
        skills_list.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Habilidade Excluida'}


class SkillList(Resource):
    def get(self):
        return skills_list

    def post(self):
        dados = json.loads(request.data)
        posicao = len(skills_list)
        dados['id'] = posicao
        skills_list.append(dados)
        return {'status': 'Sucesso', 'mensagem': 'Habilidade inserida'}, skills_list[posicao]
