import pergunta
import resposta
from pathlib import Path


# os modelos que iram debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# Aqui será definido o tema do debate
topico = pergunta.assunto()

# Define a personalidade de cada modelo e como eles vão abordar o assunto.
contexto_modelo_A = [{'role': 'system', 'content': 'fale em portugues, expanda as ideias que lhe forem apresentadas, seja breve nas explicações e finalize com uma pergunta ou ponderação'}]
contexto_modelo_B = [{'role': 'system', 'content': 'fale em portugues, discorde e apresente ideias contrárias ao que for falado pra você, seja breve nas suas explicações e finalize com uma provocação'}]

contexto_modelo_A.append({'role': 'user', 'content': topico})

while True:
    try:
        rodadas = int(input("\n Quantas rodadas o debate deve ter?"))
        break
    except ValueError:
        print("insira um valor correto")

x = 1 # Será usado pra definir o contador de rodadas

while x <= rodadas:

    print(f'\n\n{11 * "-"} Rodada {x} de {rodadas} {11 * "-"} \n\n ')
    print(f'\n\n {10 * "*"} Resposta do Modelo A {10 * "*"}\n\n')
    
    # Vai devolver a resposta em formato de string
    debatedor_1 = resposta.resolution(contexto_modelo_A, modelo_a)

    # A string retornada será o 'content' da 'message' de cada modelo
    contexto_modelo_A.append({'role': 'assistant', 'content': debatedor_1})
    contexto_modelo_B.append({'role': 'user', 'content': debatedor_1})
    # No modelo que gerou a resposta será o 'assistant'
    # No modelo que vai receber a pergunta, será o 'user'

    print(f'\n\n {10 * "*"} Resposta do Modelo B {10 * "*"}\n\n')
    
    # Abaixo o mesmo processo, só que no modelo B
    debatedor_2 = resposta.resolution(contexto_modelo_B, modelo_b)
    contexto_modelo_A.append({'role': 'user', 'content': debatedor_2})
    contexto_modelo_B.append({'role': 'assistant', 'content': debatedor_2})

    x += 1 # antes estava adicionando x + x, dobrando o valor.