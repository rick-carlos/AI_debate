import Scripts.pergunta as pergunta
import Scripts.save_file as save_file
import Scripts.debate as debate


# os modelos que iram debater
modelo_a = "gemma3:1b"
modelo_b = "gemma3:1b"

# Aqui será definido o tema do debate
topico = pergunta.assunto()

texto = debate.debate(modelo_a, modelo_b, topico)

save_file.salvar(texto)