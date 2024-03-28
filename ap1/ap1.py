from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

produtos = [
    {"Nome": "Arroz", "Descrição":"Alimento", "Preço":12.0,"Quantidade":1, "Id":str(uuid.uuid1()),}   
]

@app.route('/produtos', methods=["GET"])
def get_prod():
    try:
         return jsonify({"produtos": produtos})
    except Exception as e:
         return f"Ocoreu um erro: {str(e)}", 500


@app.route('/produtos', methods=["POST"])
def create_prod():
    try:
        # Obtém os dados do produto do corpo da solicitação JSON
        data = request.json
        # Cria um novo produto com um ID único e adiciona à lista dprodutos
        produto = {
            "Nome": data['Nome'],            
            "Descrição": data['Descrição'],
            "Preço": data['Preço'],
            "Quantidade": data["Quantidade"],
            "Id": str(uuid.uuid1()),
        }
        produtos.append(produto)
        # Retorna uma mensagem de sucesso em JSON
        return jsonify({"message": "Produto criado com sucesso!"})
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

# Rota para obter uproduto específico pelo seu ID
@app.route('/produtos/<string:prod_id>', methods=['GET'])
def get_produto(prod_id):
    try:
        # Procura o produto na lista de produtos pelo seu ID
        for p in produtos:
            if p['Id'] == prod_id:
                # Retorna produto encontrado em formato JSON
                return jsonify(p)
        # Retorna uma mensagem se o produto não for encontrado
        return "Produto não encontrado"
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

@app.route('/produtos/<string:prod_id>', methods=['PUT'])
def upd_prod(prod_id):
    try:
        # Procura o prod na lista de prodtuo pelo seu ID
        for u in produtos:
            if u['Id'] == prod_id:
                # Obtém os dados do produto do corpo da solicitação JSON
                data = request.json
                # Atualiza o nome do prod se fornecido no corpo da solicitação
                u['Nome'] = data.get('Nome', u['Nome'])
                # Retorna uma mensagem de sucesso em JSON
                return jsonify({"message": "Produto atualizado com sucesso!"})
        # Retorna uma mensagem se produto não for encontrado
        return jsonify({"error": "Produto não encontrado!"}), 404
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500

@app.route('/produtos/<string:prod_id>', methods=['PATCH'])
def pat_prod(prod_id):
    try:
        # Procura o prod na lista de prodtuo pelo seu ID
        for pat in produtos:
            if pat['Id'] == prod_id:
                # Obtém os dados do produto do corpo da solicitação JSON
                data = request.json
                # Atualiza o nome do prod se fornecido no corpo da solicitação
                pat['Nome'] = data.get('Nome', pat['Nome'])
                # Retorna uma mensagem de sucesso em JSON
                return jsonify({"message": "Produto atualizado com sucesso!"})
        # Retorna uma mensagem se produto não for encontrado
        return jsonify({"error": "Produto não encontrado!"}), 404
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500
    
@app.route('/produtos/<string:prod_id>', methods=['DELETE'])
def del_prod(prod_id):
    try:
        # Procura produto na lista produtos pelo seu ID
        for p in produtos:
            if p['Id'] == prod_id:
                # Remove produto da lista produtos
                produtos.remove(p)
                # Retorna uma mensagem de sucesso em JSON
                return jsonify({"message":"produto deletado com sucesso!"})
        # Retorna uma mensagem se produto não for encontrado
        return jsonify({"error":"produto não encontrado!"}), 404
    except Exception as e:
        # Retorna uma mensagem de erro se ocorrer algum problema
        return f"Ocorreu um erro: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)



