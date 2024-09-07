import datetime as dt

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
            

# formato em que a data e hora estão organizadas
def format_datetime():
    return "%d/%m/%Y-%H:%M:%S"


# verifica se a data de expiração ainda é válida
def is_valid(expire):
    actual_datetime = dt.datetime.now()
    if isinstance(expire, dt.datetime):
        expire_datetime = expire
    else:
        expire_datetime = dt.datetime.strptime(expire, format_datetime())
    
    if actual_datetime < expire_datetime:
        return {"result": True}
    return {"result": False, "cause": "expired"}


#organiza o tempo de expiração em segundos
def organize_expire_time_seconds(datetime, expire):
    if not is_possible_int(expire):
        error = {
            "result": "Error",
            "error_name": "attribute_expire_not_valid",
            "cause_error": "expire"
        }
        return error
        
    if int(expire) < 0:
        expire = int(expire) * -1
        
    datetime_organized = dt.datetime.strptime(datetime, format_datetime()) + dt.timedelta(seconds=int(expire))
    
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
        
    if int(expire) < 0:
        expire = int(expire) * -1
        
    datetime_organized = dt.datetime.strptime(datetime, format_datetime()) + dt.timedelta(minutes=int(expire))
   
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
        
    if int(expire) < 0:
        expire = int(expire) * -1
        
    datetime_organized = dt.datetime.strptime(datetime, format_datetime()) + dt.timedelta(hours=int(expire))
    
    data = {
        "result": "Success",
        "data": datetime_organized
    }
    return data
    

# verifica se é possível transformar um dado em inteiro
def is_possible_int(data):
    try:
        int(data)
        return True
    except:
        return False
