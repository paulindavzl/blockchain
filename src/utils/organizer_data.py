import random

# organiza uma sequência de dados de acordo com uma ordem
def organize_data(data, order, is_analyze):
    match order:
        case "top":
            organized_data = organizer_top(data)
            return organized_data
        case "bottom":
            organized_data = organizer_bottom(data)
            return organized_data
        case "random":
            organized_data = organizer_random(data, is_analyze)
            return organized_data
        case _:
            result = {
                "result": "Error",
                "error_name": "attribute_order_error",
                "cause_error": order
            }
            
            return result
            

# transforma a data de dicionário para lista
def transform_data(data):
    data_list = []
    for key in data:
        data_list.append(data.get(key))
        
    return data_list
    
    
# une todos os itens de uma lista em uma variável e codifica-a
def unite_encode_data(data_list):
    united_data = ""
    for item in data_list:
        united_data = united_data + str(item)
        
    united_data_encode = united_data.encode("utf-8")
    return united_data_encode
        

# organiza uma sequência de dados de cima para baixo
def organizer_top(data):
    data_list = transform_data(data)
    organized_data = unite_encode_data(data_list)
    
    result = {
        "result": "Success",
        "data": organized_data
    }
    
    return result
    

# organiza uma sequência de dados de baixo para cima
def organizer_bottom(data):
    data_list = transform_data(data)
    data_list.reverse()
    organized_data = unite_encode_data(data_list)
    
    result = {
        "result": "Success",
        "data": organized_data
    }
    
    return result
    
    
# organiza uma sequência de dados de forma pseudoaleatória
def organizer_random(data, is_analyze):
    data_list = transform_data(data)
    if not is_analyze:
        sequence = ""
        while True:
            sequence = list(range(len(data_list)))
            
            random.shuffle(sequence)
            if sequence != list(range(len(data_list))):
                break
    else:
        sequence = data.get("sequence")
        
    
    random_data = ""
    for turn in sequence:
        random_data = random_data + str(data_list[turn])
        
    random_data_encode = random_data.encode("utf-8")
    
    result = {
        "result": "Success",
        "sequence": sequence,
        "data": random_data_encode
    }
    
    return result