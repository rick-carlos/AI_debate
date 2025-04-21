from datetime import datetime
from pathlib import Path

def salvar(texto):

    # Esse bloco é só pra criar o nome do arquivo .txt que guardará o debate
    # O nome vai ser baseado na hora e data
    nome_do_arquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    (Path("textos") / "debates").mkdir(parents=True, exist_ok=True)

    # O arquivo vai ser guardado no diretório debates
    arquivo_de_texto = Path("textos") / "debates" / f'debate_log_{nome_do_arquivo}.txt' 
    bloco_de_texto = " ".join(texto)

    # Escreve o debate inteiro no arquivo .txt
    with open(arquivo_de_texto, 'w') as escrever_arquivo:
        escrever_arquivo.write(bloco_de_texto)