import pergunta
import resposta
from pathlib import Path
from datetime import datetime


# os modelos que iram debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# Aqui será definido o tema do debate
topico = pergunta.assunto()

# Define a personalidade de cada modelo e como eles vão abordar o assunto.
contexto_modelo_A = [{'role': 'system', 'content': 'fale em portugues, expanda as ideias que lhe forem apresentadas, seja breve nas explicações, use emojis e finalize com uma pergunta ou ponderação'}]
contexto_modelo_B = [{'role': 'system', 'content': 'fale em portugues, discorde e apresente ideias contrárias ao que for falado pra você, seja breve nas suas explicações, use emojis e finalize com uma provocação'}]

contexto_modelo_A.append({'role': 'user', 'content': topico})

while True:
    try:
        rodadas = int(input("\n Quantas rodadas o debate deve ter? "))
        break
    except ValueError:
        print("insira um valor correto")

x = 1 # Será usado pra definir o contador de rodadas

# essa lista será usada pra guardar as saídas para integrar em um arquivo só
texto = []

while x <= rodadas:

    presentation = (f'\n\n{11 * "-"} Rodada {x} de {rodadas} {11 * "-"} \n'
    f'\n\n {10 * "*"} Resposta do Modelo A {10 * "*"}\n\n')
    texto.append(presentation)
    print(presentation)
    
    # Vai devolver a resposta em formato de string
    debatedor_1 = resposta.resolution(contexto_modelo_A, modelo_a)
    texto.append(debatedor_1)

    # A string retornada será o 'content' da 'message' de cada modelo
    contexto_modelo_A.append({'role': 'assistant', 'content': debatedor_1})
    contexto_modelo_B.append({'role': 'user', 'content': debatedor_1})
    # No modelo que gerou a resposta será o 'assistant'
    # No modelo que vai receber a pergunta, será o 'user'

    presentation = f'\n\n {10 * "*"} Resposta do Modelo B {10 * "*"}\n\n'
    texto.append(presentation)
    print(presentation)
    
    # Abaixo o mesmo processo, só que no modelo B
    debatedor_2 = resposta.resolution(contexto_modelo_B, modelo_b)
    texto.append(debatedor_2)
    contexto_modelo_A.append({'role': 'user', 'content': debatedor_2})
    contexto_modelo_B.append({'role': 'assistant', 'content': debatedor_2})

    x += 1


# Esse bloco é só pra criar o nome do arquivo .txt que guardará o debate
# O nome vai ser baseado na hora e data.
nome_do_arquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
(Path("textos") / "debates").mkdir(parents=True, exist_ok=True)

# O arquivo vai ser guardado no diretório debates
arquivo_de_texto = Path("textos") / "debates" / f'debate_log_{nome_do_arquivo}.txt' 
bloco_de_texto = " ".join(texto)

# Escreve o debate inteiro no arquivo .txt
with open(arquivo_de_texto, 'w') as escrever_arquivo:
    escrever_arquivo.write(bloco_de_texto)