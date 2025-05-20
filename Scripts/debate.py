import Scripts.resposta as resposta
import Scripts.chat as chat
import Scripts.persona as persona


def debate(modelo_a, modelo_b, topico):

    if topico[1] == 'debate_entre_modelos':

        topico = topico[0]

        personalidade = persona.mind()

        # Define a personalidade de cada modelo e como eles vão abordar o assunto.
        contexto_modelo_A = [{'role': 'system', 'content': personalidade[0]}]
        contexto_modelo_B = [{'role': 'system', 'content': personalidade[1]}]

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

            devaneio = f'conecte sua resposta de volta ao tema do debate que é {topico}'

            if x % 5 == 0:
                contexto_modelo_A.append({'role': 'user', 'content': devaneio})


            presentation = (f'\n\n{11 * "-"} Rodada {x} de {rodadas} {11 * "-"} \n'
            f'\n\n {10 * "*"} Resposta do Modelo A 🤖 {10 * "*"}\n\n')
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

            presentation = f'\n\n {10 * "*"} Resposta do Modelo B 👾 {10 * "*"}\n\n'
            texto.append(presentation)
            print(presentation)
            
            # Abaixo o mesmo processo, só que no modelo B
            debatedor_2 = resposta.resolution(contexto_modelo_B, modelo_b)
            texto.append(debatedor_2)
            contexto_modelo_A.append({'role': 'user', 'content': debatedor_2})
            contexto_modelo_B.append({'role': 'assistant', 'content': debatedor_2})

            x += 1


    elif topico == 'conversar_com_modelo':
        personalidade_xat = persona.xat()
        texto = chat.chat(personalidade_xat)

    return texto