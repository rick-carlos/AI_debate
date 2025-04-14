import ollama

assistente = "gemma3:latest"

print(f"\n {10 * '*'} Assistente: Olá, sobre o que você gostaria de conversar? {10 * '*'} \n")
print(f"{10 * '-'} Digite /bye pra sair do chat {10 * '-'} \n")


while True:

    pergunta = input("\n Você :  ")

    
    if pergunta.lower() == '/bye':
        break

    else:
        
        contexto = [{'role': 'user', 'content': pergunta}]
        
        # stream=True pra printar conforme gera as palavras
        resposta = ollama.chat(model=assistente, messages=contexto, stream=True) 
        
        resposta_completa = ''

        for parte in resposta:
            chat = parte['message']['content']
            
            resposta_completa += chat

            # sem o end='', vai pular a linha pra cada palavra printada
            print(chat, end='', flush=True) # flush pra usar o stream
        
        contexto.append([{'role': 'assistant', 'content': resposta_completa}])
        
        

print(f"\n {10 * '*'} Assistente: Adeus {10 * '*'} \n")