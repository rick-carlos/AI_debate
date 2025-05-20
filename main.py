import Scripts.pergunta as pergunta
import Scripts.save_file as save_file
import Scripts.debate as db


# os modelos que irão debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# Aqui será definido o tema do debate
topico = pergunta.assunto()

# inicia a discussão e retorna todo o texto gerado no debate
texto = db.debate(modelo_a, modelo_b, topico)

# concatena a lista de textos e salva o output no diretório textos/debates
save_file.salvar(texto)