import ollama

assistente = "gemma3:latest"
contexto = []  # criado a lista de contexto fora do loop while pra ele não ser
               # recarregado toda vez.

print(f"\n {10 * '*'} Assistente: Olá, sobre o que você gostaria de conversar? {10 * '*'} \n")
print(f"{10 * '-'} Digite /bye pra sair do chat {10 * '-'} \n")


while True:

    pergunta = input("\n Você :  ")

    
    if pergunta.lower() == '/bye':
        break

    else:
        
        contexto.append({'role': 'user', 'content': pergunta})
        
        # stream =True pra printar conforme gera as palavras
        resposta = ollama.chat(model=assistente, messages=contexto, stream=True) 
        
        resposta_completa = ''

        for parte in resposta:
            if 'message' in parte: # necessário if por conta do texto inserido em resposta_completa abaixo
                chat = parte['message']['content']
                
                # o modelo vai gerar a resposta e o thinking como metadado usado que será aninhado no output
                # o thinking é armazenado em um dicionário próprio como internal thoughts ou system messages 
                # mas no stream convertido em texto, thinking será armazenado no reposta_completa tambem
                # use if pra destacar apenas os textos no dicionário 'message' e ignorar o thinking
                resposta_completa += chat

                # sem o end='', vai pular a linha pra cada palavra printada
                print(chat, end='', flush=True) # flush pra usar o stream
        
        contexto.append({'role': 'assistant', 'content': resposta_completa})

print(f"\n {10 * '*'} Assistente: Adeus {10 * '*'} \n")