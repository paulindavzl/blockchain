import hashlib
import random
import time
import datetime
from utils import organizer_data, analyze_expire
from exceptions import data_errors, command_errors, attribute_errors

# estrutura da Blockchain
class Block:
    def __init__(self, init_order="top", exception=True, expire=False, private_key=None, requirement=[2, "00"]):
        self.__init_order = init_order
        self.__exception = exception
        self.__expire = expire
        self.__private_key = private_key
        self.__is_analyze = False
        self.__status = "instantiated"
        self.__nonce = 0
        self.__hash = "undefined"
        self.__req = requirement
        
        
    # adiciona ou atualiza os dados da blockchain
    def update(self, data):
        if isinstance(data, dict):
            self.__data = data
            self.__data["init_order"] = self.__init_order
            self.__status = "updated"
            return self
            
        result = {
            "result": "Error",
            "error_name": "data_not_dict",
            "cause_error": data
        }
        raise data_errors.DataError(result)
            
    
    # gera a blockchain
    def generate(self):
        if self.__status == "instantiated":
            error = {
                "result": "Error",
                "error_name": "blockchain_not_updated",
                "command_error": "generate"
            }
            raise command_errors.CommandError(error)
        elif self.__status == "generated":
            error = {
                "result": "Error",
                "error_name": "blockchain_already_generated",
                "command_error": "generate"
            }
            raise command_errors.CommandError(error)
            
        self.__set_data()
        data = organizer_data.organize_data(self.__data, self.__init_order, self.__is_analyze)
                
        if data.get("result") == "Error":
            raise attribute_errors.AttributeError(data)
        if self.__init_order == "random":
            self.__sequence = data.get("sequence")
        
        if not self.__is_analyze:
            while self.__hash[:self.__req[0]] != self.__req[1]:
                self.__calculate_hash(data)
        else:
            self.__calculate_hash(data)
        
        self.__status = "generated"
        return self
        
    
    # calcula a hash
    def __calculate_hash(self, data):
        hash = hashlib.sha256(data.get("data"))
            
        if self.__private_key != None:
            hash.update(str(self.__private_key).encode("utf-8"))
                
        hash.update(str(self.__get_nonce()).encode("utf-8"))
        self.__hash = hash.hexdigest()
        
    
    # retorna as informações da blockchain
    def show(self):
        if self.__status == "instantiated":
            error = {
                "result": "Error",
                "error_name": "blockchain_not_updated",
                "command_error": "show"
            }
            raise command_errors.CommandError(error)
        elif self.__status == "updated":
            error = {
                "result": "Error",
                "error_name": "blockchain_not_generated",
                "command_error": "show"
            }
            raise command_errors.CommandError(error)
            
        data = self.__data
        data["hash"] = self.__hash
        data["nonce"] = self.__nonce
        if self.__req != [2, "00"]:
            data["requirement"] = self.__req
        if self.__init_order == "random":
            data["sequence"] = self.__sequence
        if self.__is_analyze:
            return data.get("hash")
        
        return data
        
        
    # obtém o nonce
    def __get_nonce(self):
        if not self.__is_analyze:
            self.__nonce += 1
        
        return self.__nonce
        
        
    # define informações variáveis
    def __set_data(self):
        if not self.__is_analyze:
            self.__set_datetime()
            
            if self.__expire:
                self.__set_expire_time()
            
            
    # define a data e a hora em que a blockchain está sendo gerada
    def __set_datetime(self):
        self.__datetime = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        self.__data["datetime"] = self.__datetime
        
        return {"result": "Success"}
        
        
    # define o tempo de expiração caso seja necessário
    def __set_expire_time(self):
        result = analyze_expire.expire(self.__datetime, self.__expire)
        if result.get("result") == "Success":
            self.__expire = result.get("data")
            self.__data["expire"] = self.__expire
            return {"result": "Success"}
        
        raise attribute_errors.AttributeError(result)
        
        
    # define os dados quando para análise
    def set_analyze_data(self, data):
        self.__is_analyze = True
        self.__private_key = data.get("private_key")
        self.__expire = data.get("expire")
        self.__requirement = data.get("requirement")
        self.__nonce = data.get("nonce")
        self.__init_order = data.get("init_order")
            
            
# analiza se a blockchain é válida
class Blockchain:
    # verifica se uma blockchain é valida
    def is_valid(self, blockchain, private_key=None):
        self.__blockchain = blockchain
        hash_analyzed = self.__blockchain.get("hash")
        expire = self.__get_expire_time()
        requirement = self.__get_requirement()
        init_order = self.__get_init_order()
        data = {
            "private_key": private_key,
            "expire": expire,
            "requirement": requirement,
            "nonce": self.__blockchain.get("nonce"),
            "init_order": init_order
        }
        
        self.__block = Block()
        self.__block.set_analyze_data(data)
        self.__generate_blockchain()
        
        hash_generated = self.__block.show()
        
        
        # compara as hashes
        if not self.__compare(hash_generated, hash_analyzed):
            result = {
                "result": False,
                "cause": "different_hashes"
            }
            
            return result
            
        if expire:
            return analyze_expire.is_valid(self.__blockchain.get("expire"))
        return {"result": True}
        
    
    # obtém a ordem em que os dados serão organizados
    def __get_init_order(self):
        if self.__blockchain.get("init_order") != None:
            return self.__blockchain.get("init_order")
        
        return "top"
        
    
    # compara as hashes
    def __compare(self, hash_ge, hash_an):
        print(hash_ge)
        print(hash_an)
        return hash_ge == hash_an
        
        
    # gera a blockchain para análise
    def __generate_blockchain(self):
        data = self.__get_data_generate()
        
        self.__block.update(data)
        self.__block.generate()
        
        
    # obtém os dados removendo informações pós geração
    def __get_data_generate(self):
        post_generation_data = [
            "hash",
            "nonce",
            "requirement"
        ]
        data = self.__blockchain
        keys = list(data.keys())
        for item in post_generation_data:
            if item in keys:
                data.pop(item)
                
        if data.get("init_order") == "random":
            if data.get("sequence") == None:
                data["sequence"] = list(range(len(data)))
        
        return data
        
    
    # verifica se tem tempo de expiração
    def __get_expire_time(self):
        if self.__blockchain.get("expire") != None:
            return self.__blockchain.get("expire")
            
        return False
        
    
    # verifica se tem alguma exigência na criação
    def __get_requirement(self):
        if self.__blockchain.get("requirement") != None:
            return self.__blockchain.get("requirement")
        
        return [2, "00"]
        