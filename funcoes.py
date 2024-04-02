from config import log

def soma(x, y):   
    """
        Função mostrando a utilização do log.
        Essa função faz a soma entre 2 números informados pelo usuário e ao realizar a soma
        junto com a classe log é informado no arquivo de log o resultado ou o erro.
    """
    try:
        log.info(float(x) + float(y))
        return str(float(x) + float(y))
    except Exception as e:
        log.erro(f'Erro de Execucao. Detalhes: {str(e)}')
        return False