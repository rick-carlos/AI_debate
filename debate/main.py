import pergunta
import resposta
from pathlib import Path


# os modelos que iram debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# devolve uma string 
topico = pergunta.assunto()

# lista usada pelo ollama pra dar contexto e uma linha histórica da discussão
debate = [{'role': 'user', 'content': topico}]

x = 1

while x <= 20:

    print(f'\n {10 * "*"} Resposta do modelo A {10 * "*"}\n')
    debatedor_1 = resposta.resolution(debate, modelo_a)
    debate.append({'role': 'user', 'content': debatedor_1})

    print(f'\n {10 * "*"} Resposta do modelo B {10 * "*"}\n')
    debatedor_2 = resposta.resolution(debate, modelo_b)
    debate.append({'role': 'assistant', 'content': debatedor_2})

    x += x