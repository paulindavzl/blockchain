import pytest
import datetime as dt
import re
import sys
import os

# adiciona o caminho do script que será testado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.analyze_expire import expire, organize_expire_time_seconds, organize_expire_time_minutes, organize_expire_time_hours

# dados usados nos testes
@pytest.fixture
def datetime():
    return "01/09/2024-21:11:00"
    
# formato da data e hora
@pytest.fixture
def format():
    return "%d/%m/%Y-%H:%M:%S"
    
# testa organizar a data de expiração em alguns segundos
def test_organize_expire_time_seconds(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-21:11:30", format)
    }
    expire_time = "30"
    
    assert organize_expire_time_seconds(datetime, expire_time) == expected_response
    

# testa organizar a data de expiração em alguns minutos
def test_organize_expire_time_minutes(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-21:13:00", format)
    }
    expire_time = "2"
    
    assert organize_expire_time_minutes(datetime, expire_time) == expected_response
    

# testa organizar a data de expiração em algumas horas
def test_organize_expire_time_hours(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-22:11:00", format)
    }
    expire_time = "1"
    
    assert organize_expire_time_hours(datetime, expire_time) == expected_response
    

# testa a função que gerencia a expiração com segundos sem "s"
def test_expire_second_not_s(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-21:13:00", format)
    }
    expire_time = "120"
    
    assert expire(datetime, expire_time) == expected_response
    
    
# testa a função que gerencia a expiração com segundos com "s"
def test_expire_seconds(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-21:14:10", format)
    }
    expire_time = "190s"
    
    assert expire(datetime, expire_time) == expected_response
    
    
# testa a função que gerencia a expiração com minutos
def test_expire_minutes(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("01/09/2024-22:11:00", format)
    }
    expire_time = "60m"
    
    assert expire(datetime, expire_time) == expected_response
    
    
# testa a função que gerencia a expiração com horas
def test_expire_hours(datetime, format):
    expected_response = {
        "result": "Success",
        "data": dt.datetime.strptime("02/09/2024-21:11:00", format)
    }
    expire_time = "24h"
    
    assert expire(datetime, expire_time) == expected_response
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_analyze_expire.py"])