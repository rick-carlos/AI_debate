import ollama

assistente = "gemma3:latest"
contexto = []

print(f"\n {10 * '*'} Assistente: Olá, sobre o que você gostaria de conversar? {10 * '*'} \n")
print(f"{10 * '-'} Digite /bye pra sair do chat {10 * '-'} \n")


while True:

    pergunta = input("\n Você :  ")

    
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

print(f"\n {10 * '*'} Assistente: Adeus {10 * '*'} \n")