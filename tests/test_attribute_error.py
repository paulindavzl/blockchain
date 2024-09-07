import pytest
import re
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.exceptions.attribute_errors import AttributeError

# dados usados nos testes
@pytest.fixture
def data():
    data_test = {
        "result": "Error",
        "cause_error": "other"
    }
    
    return data_test 

# retorna a mensagem de erro de acordo com o nome do erro
def get_message_error(data):
    error_name = data.get("error_name")
    cause_error = data.get("cause_error")
    
    errors = {
        "attribute_order_error": f"The order you set ({cause_error}) is not accepted. Use 'top', 'bottom' or 'random'. See documentation at github.com/paulindavzl/blockchain",
        "attribute_exception_error": f"'{cause_error}' is not accepted as a value for 'exception'. Set to True or False. See documentation at github.com/paulindavzl/blockchain",
        "attribute_expire_not_valid": "The value assigned to expire is invalid! See documentation at github.com/paulindavzl/blockchain",
        "requirement_not_str": f"The value of the requirement attribute must be string. '{cause_error}' is not string. See documentation at github.com/paulindavzl/blockchain",
            "requirement_not_valid": f"The requirement attribute only accepts lowercase letters or numbers! '{cause_error}' is invalid. See documentation at github.com/paulindavzl/blockchain"
    }
    
    error = errors.get(error_name)
    return error
    

# testa o erro de atribuir um valor não aceito à init_order (Blockchain)
def test_attribute_order_error(data):
    data["error_name"] = "attribute_order_error"
    expected_message_error = re.escape(get_message_error(data))
    class_error = AttributeError(data)
    
    with pytest.raises(AttributeError, match=expected_message_error):
        raise class_error
        
        
# testa o erro de atribuir um valor não aceito à exception (Blockchain)
def test_attribute_exception_error(data):
    data["error_name"] = "attribute_exception_error"
    expected_message_error = re.escape(get_message_error(data))
    class_error = AttributeError(data)
    
    with pytest.raises(AttributeError, match=expected_message_error):
        raise class_error
        

# testa o erro de atribuir um valor não aceito à exception (Blockchain)
def test_attribute_expire_not_valid(data):
    data["error_name"] = "attribute_expire_not_valid"
    expected_message_error = re.escape(get_message_error(data))
    class_error = AttributeError(data)
    
    with pytest.raises(AttributeError, match=expected_message_error):
        raise class_error
        
        
# testa o valor de requirement diferente de string (Blockchain)
def test_attribute_requirement_not_str(data):
    data["error_name"] = "requirement_not_str"
    data["cause_error"] = 10
    expected_message_error = re.escape(get_message_error(data))
    class_error = AttributeError(data)
    
    with pytest.raises(AttributeError, match=expected_message_error):
        raise class_error
        
        
# testa os valores de requirement (Blockchain)
def test_attribute_requirement_not_valid(data):
    data["error_name"] = "requirement_not_valid"
    data["cause_error"] = "0 "
    expected_message_error = re.escape(get_message_error(data))
    class_error = AttributeError(data)
    
    with pytest.raises(AttributeError, match=expected_message_error):
        raise class_error


if __name__ == "__main__":
    pytest.main(["-vv", "test_attribute_error.py"])