import pytest
import re
import time
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.blockchain import Block

# dados usados nos testes
@pytest.fixture
def data():
    data_test = {
        "id": 1,
        "name": "Teste",
        "private_key": "PRIVATE_KEY",
        "previous_hash": "GenerateHash",
        "id_previous_hash": 0
    }
    
    return data_test
    

# testa fazer update nos dados para a blockchain
def test_blockchain_update(data):
    blockchain = Block()
    
    assert blockchain.update(data) == blockchain
    

# testa gerar a blockchain sem chave privada e sem expiração
def test_blockchain_generate_n_pky_n_exp(data):
    blockchain = Block()
    blockchain.update(data)
    
    assert blockchain.generate() == blockchain
    

# testa gerar a blockchain com chave privada e sem expiração
def test_blockchain_generate_pky_n_exp(data):
    blockchain = Block(private_key = "012345678")
    blockchain.update(data)
    
    assert blockchain.generate() == blockchain
    

# testa gerar a blockchain sem chave privada e com expiração
def test_blockchain_generate_n_pky_exp(data):
    blockchain = Block(expire = "30s")
    blockchain.update(data)
    
    assert blockchain.generate() == blockchain


# testa gerar a blockchain com chave privada e com expiração
def test_blockchain_generate_pky_exp(data):
    blockchain = Block(expire = "1m", private_key = "012345678")
    blockchain.update(data)
    
    assert blockchain.generate() == blockchain
    

# testa mostrar os dados da blockchain
def test_blockchain_show(data):
    blockchain = Block()
    blockchain.update(data)
    blockchain.generate()
    
    assert blockchain.show() == data
    
    
    
if __name__ == "__main__":
    pytest.main(["-vv", "test_blockchain.py"])