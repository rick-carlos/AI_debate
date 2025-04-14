import ollama

# chama o modelo baixado no ollama
modelo = "gemma3:1b"

# a pergunta que será feita pro modelo
pergunta = input("o que você quer saber? : ")

# Isso é uma lista de dicionários que serão usados pra dar contexto
# e uma continuidade da conversa pro modelo, cada resposta do modelo pode ser 
# incorporada na lista usando append.
contexto = [{'role': 'user', 'content': pergunta}]

# chama o modelo, passa o contexto e armazena a saída em uma variável
resposta = ollama.chat(model=modelo, messages=contexto)

# A saída do modelo será uma estrutura de dados e não apenas a reposta crua da pergunta
# Pra ter só o texto da resposta, procure diretamente o conteudo armazenado na variável reposta
mensagem = resposta['message']['content']

# printa a resposta
print(mensagem)
