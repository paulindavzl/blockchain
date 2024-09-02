import pytest
import re
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.exceptions.command_errors import CommandError

# dados usados nos testes
@pytest.fixture
def data():
    data_test = {
        "id": 101,
        "name": "Teste"
    }
    
    return data_test
    
# base do erro usado nos testes
@pytest.fixture
def error():
    error_test = {
        "result": "Error"
    }
    
# retorna a mensagem de erro de acordo com o nome do mesmo
def get_message_error(data):
    error_name = data.get("error_name")
    command_error = data.get("command_error")
    
    errors = {
        "blockchain_not_generate": f"Block().{command_error}() can only be used after the blockchain is generated! Use Block().generate(). See documentation at github.com/paulindavzl/blockchain",
        "blockchain_already_generate": "The blockchain has already been generated! Use Block().update() to update the data and generate a new one. See documentation at github.com/paulindavzl/blockchain",
        "blockchain_not_updated": f"Block().{command_error}() can only be used after the blockchain data has been updated! Use Block().update(). See documentation at github.com/paulindavzl/blockchain"
    }
    
    error = errors.get(error_name)
    return error
    

# testa o erro de tentar gerar a blockchain sem atualizar os dados
def test_blockchain_not_updated_gen(data):
    data["error_name"] = "blockchain_not_updated"
    data["command_error"] = "generate"
    expected_message_error = re.escape(get_message_error(data))
    class_error = CommandError(data)
    
    with pytest.raises(CommandError, match = expected_message_error):
        raise class_error
        

# testa o erro de tentar gerar a mesma blockchain duas vezes
def test_blockchain_already_generate(data):
    data["error_name"] = "blockchain_already_generate"
    data["command_error"] = "generate"
    expected_message_error = re.escape(get_message_error(data))
    class_error = CommandError(data)
    
    with pytest.raises(CommandError, match = expected_message_error):
        raise class_error
        

# testa o erro de tentar mostrar a blockchain sem atualizar os dados
def test_blockchain_not_updated_show(data):
    data["error_name"] = "blockchain_not_updated"
    data["command_error"] = "show"
    expected_message_error = re.escape(get_message_error(data))
    class_error = CommandError(data)
    
    with pytest.raises(CommandError, match = expected_message_error):
        raise class_error
        
        
# testa o erro de tentar mostrar a blockchain sem gerá-la
def test_blockchain_not_generate_show(data):
    data["error_name"] = "blockchain_not_generate"
    data["command_error"] = "show"
    expected_message_error = re.escape(get_message_error(data))
    class_error = CommandError(data)
    
    with pytest.raises(CommandError, match = expected_message_error):
        raise class_error
        

if __name__ == "__main__":
    pytest.main(["-vv", "test_command_errors.py"])