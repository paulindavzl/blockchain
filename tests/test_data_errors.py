import pytest
import re
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.exceptions.data_errors import DataError

# dados que serão usados nos testes
@pytest.fixture
def data():
    data_test = {
        "result": "Error",
        "cause_error": "str"
    }
    
    return data_test
    
# retorna uma mensagem de erro dependendo do nome
def get_message_error(data):
    cause_error = data.get("cause_error")
    error_name = data.get("error_name")
    
    errors = {
        "data_not_dict": f"The data passed to 'update' must be a dictionary. '{cause_error}' is not a dictionary."
    }
    
    error = errors.get(error_name)
    return error
    

# testa o erro gerado ao usar um dado que não e dicionário
def test_data_not_dict_error(data):
    data["error_name"] = "data_not_dict"
    expected_message_error = re.escape(get_message_error(data))
    class_error = DataError(data)
    
    with pytest.raises(DataError, match=expected_message_error):
        raise class_error
        

if __name__ == "__main__":
    pytest.main(["-vv", "test_data_errors.py"])