from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"nome": "Thiago", "id": 1, "email": "thiago.reis27@outlook.com"}   
]

# Rota para obter todos os usuários
@app.route('/users', methods=["GET"])
def get_users():
    try:
        # Retorna a lista de usuários no formato JSON
        return jsonify({"usuarios": usuarios})
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Rota para criar um novo usuário
@app.route('/users', methods=["POST"])
def create_user():
    try:
        # Obtém os dados do usuário do corpo da solicitação JSON
        data = request.json
        # Cria um novo usuário com um ID único e adiciona à lista de usuários
        usuario = {
            "id": len(usuarios) + 1,
            "nome": data['nome'],
            "email": data['email']
        }
        usuarios.append(usuario)
        # Retorna uma mensagem de sucesso em JSON
        return jsonify({"message": "Usuário criado com sucesso!"})
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Rota para obter um usuário específico pelo seu ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Procura o usuário na lista de usuários pelo seu ID
        for p in usuarios:
            if p['id'] == user_id:
                # Retorna o usuário encontrado em formato JSON
                return p
        # Retorna uma mensagem se o usuário não for encontrado
        return "Usuário não encontrado"
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Rota para atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def upd_user(user_id):
    try:
        # Procura o usuário na lista de usuários pelo seu ID
        for u in usuarios:
            if u['id'] == user_id:
                # Obtém os dados do usuário do corpo da solicitação JSON
                data = request.json
                # Atualiza o nome do usuário se fornecido no corpo da solicitação
                u['nome'] = data.get('nome', u['nome'])
                # Retorna uma mensagem de sucesso em JSON
                return jsonify({"message": "Usuário atualizado com sucesso!"})
        # Retorna uma mensagem se o usuário não for encontrado
        return jsonify({"error": "Usuário não encontrado!"}), 404
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Rota para excluir um usuário existente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def del_user(user_id):
    try:
        # Procura o usuário na lista de usuários pelo seu ID
        for u in usuarios:
            if u['id'] == user_id:
                # Remove o usuário da lista de usuários
                usuarios.remove(u)
                # Retorna uma mensagem de sucesso em JSON
                return jsonify({"message": "Usuário deletado com sucesso!"})
        # Retorna uma mensagem se o usuário não for encontrado
        return jsonify({"error": "Usuário não encontrado!"}), 404
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
