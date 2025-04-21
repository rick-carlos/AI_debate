import ollama

def resolution(lista_debate, modelo):
        
    lista_debate
    resposta = ollama.chat(model=modelo,messages=lista_debate,stream=True)
    resposta_completa = ''

    for parte in resposta:
        
        if 'message' in parte:
            
            chat = parte['message']['content']
            resposta_completa += chat
            print(chat, end='', flush=True)
        
    return resposta_completa

