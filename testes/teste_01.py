import requests

def test_status_api_reqres():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    status = response.status_code
    assert status == 200, f"Erro: Esperado status 200, mas obteve {status}"
    print("✅ Teste 01 passou com sucesso - Status 200 recebido")

# Executar o teste
test_status_api_reqres()

