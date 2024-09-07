import pytest
import re
import time
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.blockchain import Block, Blockchain

# dados usados nos testes
@pytest.fixture
def data():
    data_test = {
        "id": 1,
        "name": "Teste"
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
    
    assert blockchain.show().get("result") == data.get("result")
    

# testa se a blockchain é válida
def test_blockchain_is_valid(data):
    block = Block(expire="30s")
    block.update(data).generate()
    hash = block.show()
    
    assert Blockchain().is_valid(hash).get("result")
    

# testa se a blockchain é inválida por expiração
def test_blockchain_not_is_valid_exp(data):
    block = Block(expire="1")
    block.update(data).generate()
    hash = block.show()
    
    # aguarda até a blockchain expirar
    time.sleep(1.01)
    
    assert Blockchain().is_valid(hash).get("cause") == "expired"
    

# testa se a blockchain é inválida por alteração em algum dado
def test_blockchain_not_is_valid_hashes(data):
    block = Block(expire="30")
    block.update(data).generate()
    hash = block.show()
    
    # modifica a blockchain
    hash["name"] = "Testee"
    
    assert Blockchain().is_valid(hash).get("cause") == "different_hashes"
    
    
# testa gerar e validar com private_key
def test_blockchain_generate_valid_private_key(data):
    PRIVATE_KEY = "1234"
    block = Block(expire="30s", private_key=PRIVATE_KEY)
    block.update(data).generate()
    hash = block.show()
    
    assert Blockchain().is_valid(hash, private_key=PRIVATE_KEY).get("result")
    
    
# testa gerar com private_key e validar sem
def test_blockchain_generate_valid_not_private_key(data):
    PRIVATE_KEY = "1234"
    block = Block(expire="30s", private_key=PRIVATE_KEY)
    block.update(data).generate()
    hash = block.show()
    
    assert not Blockchain().is_valid(hash).get("result")
    
    
# testa validar com uma private_key diferente
def test_blockchain_invalid_private_key(data):
    PRIVATE_KEY = "1234"
    block = Block(expire="30s", private_key=PRIVATE_KEY)
    block.update(data).generate()
    hash = block.show()
    
    assert not Blockchain().is_valid(hash, private_key="1235").get("result")
    
    
# testa gerar sem private_key e validar usando uma
def test_blockchain_valid_private_key(data):
    PRIVATE_KEY = "1234"
    block = Block(expire="30s")
    block.update(data).generate()
    hash = block.show()
    
    assert not Blockchain().is_valid(hash, private_key=PRIVATE_KEY).get("result")
    
    
if __name__ == "__main__":
    pytest.main(["-vv", "test_blockchain.py"])