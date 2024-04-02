from datetime import datetime
import os

class Log:   

    def __init__(self, caminho):
        """ Inicializando a classe deverá ser passado a pasta onde será criado a pasta de logs. """
        self._data = datetime.today().strftime('%d-%m-%Y')
        self._caminho = caminho
    
    #privando métodos que usarei dentro da classe

    def _criar_pasta(self):
        """ 
            Cria o diretório onde serão armazenados os logs, o diretório será criado 
            no atributo caminho que foi passado na istância da classe como um novo diretório com o 
            nome de LOGS, e será onde os arquivos ficarão registrados.
        """
        dir_path = os.path.join(self._caminho, 'LOGS')
        os.makedirs(dir_path, exist_ok=True)
        return dir_path

    def _definir_nome_arquivo(self):
        """
            Ajustando o nome do arquivo onde será escrito os logs, nome sempre sera dia-mes-ano 
            atual do momento que o arquivo log for iniciado/criado.
        """
        nome_pasta = self._criar_pasta()
        nome_arquivo = os.path.join(nome_pasta, self._data + '.txt')
        return nome_arquivo


    def _escrever_log(self, nivel, msg):
        """ 
            Método que irá escrever no arquivo de Log, inserindo o começo da mensagem,
            com base no dia e nível que está sendo chamado nos métodos abaixo junto
            com a mensagem.
            Com o with open no modo 'append' ele continuará inserindo no mesmo arquivo de logs
            durante a execução diária.
        """
        nome_arquivo = self._definir_nome_arquivo()
        data_hora = datetime.now().strftime('[%d/%m/%Y %H:%M:%S]')
        try:
            with open(nome_arquivo, 'a') as log_file:
                log_file.write(f"{data_hora} {nivel}: {msg}\n")
            return 'LOG escrito com sucesso'
        except Exception as e:
            print(e)
            raise Exception('Erro ao escrever no arquivo de LOG')

    # Métodos que serão chamados pelo usuário para escrever no log
        
    def info(self, msg):
        """ Escreve no arquivo de Logs uma mensagem do nível 'INFO' """
        return self._escrever_log("INFO", msg)

    def erro(self, msg):
        """ Escreve no arquivo de Logs uma mensagem do nível 'ERRO' """
        return self._escrever_log("ERRO", msg)

    def sucesso(self, msg):
        """ Escreve no arquivo de Logs uma mensagem do nível 'SUCESSO' """
        return self._escrever_log("SUCESSO", msg)