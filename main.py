import pergunta
import resposta
import chat
import save_file


# os modelos que iram debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# Aqui será definido o tema do debate
topico = pergunta.assunto()

if topico[1] == 'debate_entre_modelos':

    topico = topico[1]

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

elif topico == 'conversar_com_modelo':
    texto = chat.chat()

save_file.salvar(texto)