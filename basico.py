import ollama

assistente = "gemma3:latest"

print(f"\n {10 * '*'} Assistente: Olá, sobre o que você gostaria de conversar? {10 * '*'} \n")
print(f"{10 * '-'} Digite /bye pra sair do chat {10 * '-'} \n")

while True: # Sem um loop while, o modelo responderia apenas 1 pergunta.

    pergunta = input("Você :  ")

    # palavra chave pra sair do chat
    if pergunta.lower() == '/bye':  # Diminuindo todas as letras pra caso o user digite bye com CAPSLOCK
        break

    else:
        contexto = [{'role': 'user', 'content': pergunta}]

        resposta = ollama.chat(model=assistente, messages=contexto)

        mensagem = resposta['message']['content']

        print(f'Assistente: {mensagem}')

        contexto.append(resposta)


print(f"\n {10 * '*'} Assistente: Adeus {10 * '*'} \n")