# exceção para definições de atributos
class AttributeError(Exception):
    def __init__(self, error):
        self.__create_messages_errors(error.get("cause_error"))
        message = self.__messages_errors.get(error.get("error_name"))
        super().__init__(message)
        
    # cria um dicionário com as mensagens de erro
    def __create_messages_errors(self, error):
        self.__messages_errors = {
            "attribute_order_error": f"The order you set ({error}) is not accepted. Use 'top', 'bottom' or 'random'. See documentation at github.com/paulindavzl/blockchain",
            "attribute_exception_error": f"'{error}' is not accepted as a value for 'exception'. Set to True or False. See documentation at github.com/paulindavzl/blockchain",
            "attribute_expire_not_valid": "The value assigned to expire is invalid! See documentation at github.com/paulindavzl/blockchain",
            "requirement_not_str": f"The value of the requirement attribute must be string. '{error}' is not string. See documentation at github.com/paulindavzl/blockchain",
            "requirement_not_valid": f"The requirement attribute only accepts lowercase letters or numbers! '{error}' is invalid. See documentation at github.com/paulindavzl/blockchain"
        }