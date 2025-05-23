# testes/teste_02.py (versão para Colab/Jupyter)

import requests

def test_json_api_jsonplaceholder():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()
    assert data["id"] == 1, f"Erro: Esperado id=1, mas obteve id={data['id']}"
    print("✅ Teste 02 passou com sucesso - ID retornado é 1")

# Executar o teste
test_json_api_jsonplaceholder()
