import unittest
from postman.meuApp import meuApp  # Importa a aplicação Flask que será testada

class TestGetUser(unittest.TestCase):
    def setUp(self):
        self.app = meuApp.test_client()  # Configura o cliente de teste antes de cada teste

    def test_get_all_users(self):
        # Testa a rota para obter todos os usuários
        response = self.app.get('/users')  # Faz uma solicitação GET para a rota de todos os usuários
        self.assertEqual(200, response.status_code)  # Verifica se a resposta é bem-sucedida (status code 200)

    def test_get_existing_user(self):
        # Testa a rota para obter um usuário específico
        response = self.app.get('/users/1')  # Faz uma solicitação GET para a rota de um usuário específico (neste caso, o ID 1)
        data = response.json  # Extrai os dados da resposta JSON
        # Verifica se os dados retornados são do tipo dicionário (representando um usuário)
        self.assertEqual(dict, type(data))
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é bem-sucedida (status code 200)
        self.assertEqual(data['id'], 1)  # Verifica se o ID do usuário retornado é o esperado (neste caso, 1)

if __name__ == '__main__':
    unittest.main()  # Executa os testes unitários ao executar o script diretamente
