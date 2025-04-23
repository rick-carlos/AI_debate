import ollama



def chat(personalidade_xat):

    assistente = "gemma3:latest"
    contexto = []
    contexto.append({'role': 'assistant', 'content': personalidade_xat})

    print(f"\n {10 * '*'} Assistente: Olá, sobre o que você gostaria de conversar? {10 * '*'} \n")
    print(f"{10 * '-'} Digite /bye pra sair do chat {10 * '-'} \n")

    bloco_de_texto = []
    
    # As variáveis abaixo são só pra demarcar quem está falando quando a conversa for 
    # salva no bloco de texto.
    usuario = 'Você: \n'
    modelo = "Assistente: \n"
    separador = '\n\n'

    while True:

        pergunta = input("\n\n Você :  ")

        bloco_de_texto.extend([usuario, pergunta, separador])

        
        if pergunta.lower() == '/bye':
            
            break

        else:
            
            contexto.append({'role': 'user', 'content': pergunta})
            
            resposta = ollama.chat(model=assistente, messages=contexto, stream=True) 
            
            resposta_completa = ''

            for parte in resposta:
                if 'message' in parte: # necessário if por conta do texto inserido em resposta_completa abaixo
                    chat = parte['message']['content']
                    
                    resposta_completa += chat

                    print(chat, end='', flush=True)
            
            contexto.append({'role': 'assistant', 'content': resposta_completa})
            bloco_de_texto.extend([modelo, resposta_completa, separador])

    print(f"\n {10 * '*'} Assistente: Adeus {10 * '*'} \n")
    return bloco_de_texto