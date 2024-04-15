# Classe Log

A classe `Log` é uma ferramenta simples de logging para Python que permite a criação e a manipulação de arquivos de log. Esses logs ajudam a documentar mensagens de erro, informações e sucessos de processos executados ao longo do tempo.

## Funcionalidades

- Criação automática de diretórios e arquivos de log baseados na data atual.
- Escrita de logs com níveis diferenciados (INFO, ERRO, SUCESSO).
- Armazenamento organizado por datas para fácil consulta.

## Como usar

1. **Instância da Classe**
   - A classe precisa ser instanciada com um caminho de diretório onde os logs serão salvos.

```python
from log import Log

# Substitua 'caminho_para_logs' pelo caminho desejado no seu sistema
logger = Log('caminho_para_logs')
```

2. **Escritas de Logs**
  - Você pode escrever logs nos níveis INFO, ERRO, e SUCESSO.
```python
# Logando informações
logger.info('Este é um log de informação.')

# Logando erros
logger.erro('Este é um log de erro.')

# Logando sucessos
logger.sucesso('Este é um log de sucesso.')
```
# Estrutura do Diretório de Logs
Os logs são salvos em um diretório LOGS dentro do caminho fornecido na instância da classe. 
Cada arquivo de log é nomeado com a data do dia em que foi criado, no formato dd-mm-yyyy.txt, 
e os logs são adicionados sequencialmente ao arquivo correspondente ao dia.

# Tratamento de Erros
A classe Log trata internamente os possíveis erros de escrita nos arquivos de log e lança exceções quando algo impede a escrita correta no arquivo.

# Requisitos
Python 3.11+

# Autor
Seu Nome ou seu Nickname - Desenvolvedor
