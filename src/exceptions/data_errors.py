# exceções nos dados fornecidos à blockchain
class DataError(Exception):
    def __init__(self, error):
        self.__create_messages_errors(error.get("cause_error"))
        message = self.__messages_errors.get(error.get("error_name"))
        super().__init__(message)
        
    # cria um dicionário com as mensagens de erro
    def __create_messages_errors(self, error):
        self.__messages_errors = {
            "data_not_dict": f"The data passed to 'update' must be a dictionary. '{error}' is not a dictionary. See documentation at github.com/paulindavzl/blockchain"
        }