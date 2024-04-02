from config import log
import funcoes as func

# Exemplo de funcionalidade da classe Log

log.info('Iniciando Processo')

resultado = func.soma(12, '7', log)
if resultado:
    log.sucesso('Processo Encerrado')

