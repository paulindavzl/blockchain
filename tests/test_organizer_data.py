import pytest
import re
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.organizer_data import organizer_top, organizer_bottom, organizer_random, organize_data

# dados usados nos testes
@pytest.fixture
def data():
    data_test = {
        "id": 10001,
        "name": "Teste",
        "email": "test@test.com",
        "password": "teste123",
        "datetime": "00/00/0000-00:00:00"
    }
    
    return data_test

# testa a organização de cima para baixo
def test_organizer_top(data):
    expected_return = {
        "result": "Success",
        "data": "10001Testetest@test.comteste12300/00/0000-00:00:00".encode("utf-8")
    }
    
    assert organizer_top(data) == expected_return
    
# testa a organização de baixo para cima
def test_organizer_bottom(data):
    expected_return = {
        "result": "Success",
        "data": "00/00/0000-00:00:00teste123test@test.comTeste10001".encode("utf-8")
    }
    
    assert organizer_bottom(data) == expected_return
    
# testa a organização aleatória para análise
def test_organizer_random_analyze(data):
    data["sequence"] = [0, 3, 4, 2, 1]
    expected_return = {
        "result": "Success",
        "sequence": [0, 3, 4, 2, 1],
        "data": "10001teste12300/00/0000-00:00:00test@test.comTeste".encode("utf-8")
    }
    
    assert organizer_random(data, True) == expected_return
    
# testa a organização aleatória sem análise
def test_organizer_random_not_analyze(data):
    expected_return = {
        "result": "Success",
        "sequence": [0, 1, 2, 3, 4],
        "data": "10001Testetest@test.comteste12300/00/0000-00:00:00".encode("utf-8")
    }
    
    assert organizer_random(data, False) != expected_return
    
# testa a função que gerencia as ordens e retorna um erro
def test_organizer_data(data):
    data["sequence"] = [0, 3, 4, 2, 1]
    
    assert organize_data(data, "top", False).get("result") == "Success"
    assert organize_data(data, "bottom", False).get("result") == "Success"
    assert organize_data(data, "random", False).get("result") == "Success"
    assert organize_data(data, "random", True).get("result") == "Success"
    assert organize_data(data, "other", False).get("result") == "Error"
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_organizer_data.py"])