import datetime

# analisa o tempo de expiração da blockchain e organiza-o
def expire(datetime, expire):
    if is_possible_int(expire):
        result = organize_expire_time_seconds(datetime, expire)
        return result
    
    # verifica o último caractére
    match expire[len(expire) - 1]:
        case "s":
            result = organize_expire_time_seconds(datetime, expire.replace("s", ""))
            return result
        case "m":
            result = organize_expire_time_minutes(datetime, expire.replace("m", ""))
            return result
        case "h":
            result = organize_expire_time_hours(datetime, expire.replace("h", ""))
            return result
        case _:
            error = {
                "result": "Error",
                "error_name": "attribute_expire_not_valid",
                "cause_error": "expire"
            }
            return error
            

# verifica se a data de expiração ainda é válida
def is_valid(expire):
    actual_datetime = get_datetime()
    
    return compare_datetimes(expire, actual_datetime)
    
    
# compara a data de expiração com a data atual
def compare_datetimes(expire, actual_datetime):
    format_datetime = "%d/%m/%Y-%H:%M:%S"
    print(expire)
    try:
        c_expire = datetime.datetime.strptime(expire, format_datetime)
        c_datetime = datetime.datetime.strptime(actual_datetime, format_datetime)
        
        result = c_expire > c_datetime
        if result:
            return {"result": True}
            
        return {"result": False, "cause": "expired"}
        
    except:
        return {"result": False, "cause": "expire_inválid"}
    

# obtém a data e a hora
def get_datetime():
    actual_datetime = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    return actual_datetime


#organiza o tempo de expiração em segundos
def organize_expire_time_seconds(datetime, expire):
    if not is_possible_int(expire):
        error = {
            "result": "Error",
            "error_name": "attribute_expire_not_valid",
            "cause_error": "expire"
        }
        return error
        
    datetime_separated = separate_datetime(datetime)
    datetime_separated["seconds"] += int(expire)
    datetime_organized = rearrange_datetime(datetime_separated)
    
    data = {
        "result": "Success",
        "data": datetime_organized
    }
    return data
    
    
#organiza o tempo de expiração em minutos
def organize_expire_time_minutes(datetime, expire):
    if not is_possible_int(expire):
        error = {
            "result": "Error",
            "error_name": "attribute_expire_not_valid",
            "cause_error": "expire"
        }
        return error
        
    datetime_separated = separate_datetime(datetime)
    datetime_separated["minutes"] += int(expire)
    datetime_organized = rearrange_datetime(datetime_separated)
   
    data = {
         "result": "Success",
         "data": datetime_organized
     }
    return data
    
    
#organiza o tempo de expiração em minutos
def organize_expire_time_hours(datetime, expire):
    if not is_possible_int(expire):
        error = {
            "result": "Error",
            "error_name": "attribute_expire_not_valid",
            "cause_error": "expire"
        }
        return error
        
    datetime_separated = separate_datetime(datetime)
    datetime_separated["hours"] += int(expire)
    datetime_organized = rearrange_datetime(datetime_separated)
    
    data = {
        "result": "Success",
        "data": datetime_organized
    }
    return data


# reorganiza da data e hora para o formato aceito
def rearrange_datetime(datetime):
    while True:
        if datetime.get("seconds") >= 60:
            datetime["seconds"] -= 60
            datetime["minutes"] += 1
        elif datetime.get("minutes") >= 60:
            datetime["minutes"] -= 60
            datetime["hours"] += 1
        elif datetime.get("hours") >= 24:
            datetime["hours"] -= 24
            datetime["day"] += 1
        elif datetime.get("month") == 2 and datetime.get("day") >= 28:
            datetime["day"] -= 28
            datetime["month"] += 1
        elif datetime.get("day") >= 30:
            datetime["day"] -= 30
            datetime["month"] += 1
        elif datetime.get("month") >= 13:
            datetime["month"] -= 13
            datetime["year"] += 1
        else:
            break
            
    datetime_str = parse_data_str(datetime)
    datetime_organized = f"{datetime_str.get('day')}/{datetime_str.get('month')}/{datetime_str.get('year')}-{datetime_str.get('hours')}:{datetime_str.get('minutes')}:{datetime_str.get('seconds')}"
    
    return datetime_organized
    
    
# transforma dados inteiros em strings
def parse_data_str(data):
    for item in data:
        data[item] = str(data.get(item))
        if item != "year" and len(data.get(item)) == 1:
            data[item] = "0" + data.get(item)
        else:
            if len(data.get(item)) == 1:
                data[item] = "000" + data.get(item)
     
    return data


# separa as informações de uma data
def separate_datetime(datetime):
    day = datetime[:2]
    month = datetime[3:5]
    year = datetime[6:10]
    hours = datetime[11:13]
    minutes = datetime[14: 16]
    seconds = datetime[17:]
    
    data = {
        "day": day,
        "month": month,
        "year": year,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
    
    new_data =  is_correct_datetime(data)
    data_int = transform_data_int(new_data)
        
    return data_int
    
    
# verifica se os dados da data e hora
def is_correct_datetime(datetime):
    for item in datetime:
        try:
            int(datetime.get(item))
        except:
            if item != "year":
                datetime[item] = "00"
            else:
                datetime[item] = "0000"
            return datetime
    
    return datetime
 


# transforma todos os itens de um dicionário em inteiro
def transform_data_int(data):
    for item in data:
        data[item] = int(data.get(item))
    
    return data
    

# verifica se é possível transformar um dado em inteiro
def is_possible_int(data):
    try:
        int(data)
        return True
    except:
        return False
