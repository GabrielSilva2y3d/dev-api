from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id': '0',
        'nome': 'Gabriel',
        'Habilidades': ['Python', 'Flask']},

    {
        'id': '1',
        'nome': 'Rafael',
        'Habilidades': ['PHP', 'JavaScript']},

    {
        'id': '2',
        'nome': 'Lala',
        'Habilidades': ['java', 'Ruby', 'C#', 'TypeScript']}

]


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor de  ID {} não existe', format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status: sucesso', 'mensagem: registro excluido'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro inserido'},
                       devs[posicao])

    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)
