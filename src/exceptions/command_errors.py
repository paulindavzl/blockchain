# classe que executa o erro
class CommandError(Exception):
    def __init__(self, error):
        self.__create_messages_errors(error.get("command_error"))
        message = self.__messages_errors.get(error.get("error_name"))
        super().__init__(message)
        
    # cria um dicionário com as mensagens de erro
    def __create_messages_errors(self, error):
        self.__messages_errors = {
            "blockchain_not_generate": f"Block().{error}() can only be used after the blockchain is generated! Use Block().generate(). See documentation at github.com/paulindavzl/blockchain",
            "blockchain_already_generate": "The blockchain has already been generated! Use Block().update() to update the data and generate a new one. See documentation at github.com/paulindavzl/blockchain",
            "blockchain_not_updated": f"Block().{error}() can only be used after the blockchain data has been updated! Use Block().update(). See documentation at github.com/paulindavzl/blockchain"
        }
        