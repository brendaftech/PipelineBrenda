from app import app 

  

  

def test_pagina_inicial(): 

    resposta = app.test_client().get("/") 

    assert resposta.status_code == 200 

    assert "Fatec" in resposta.get_json()["mensagem"] 

  

  

def test_busca_de_alunos_por_nome(): 

    resposta = app.test_client().get("/alunos?nome=an") 

    assert resposta.status_code == 200 

    assert resposta.get_json() == ["Ana", "Daniel"] 