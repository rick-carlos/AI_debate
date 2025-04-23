from pathlib import Path


# Verifica se existe o arquivo persona_A e persona_B que será usado pra definir
# a personalidade de ambos os modelos, se não existir, cria um com uma personalidade padrão.
def mind():

    while True:

        personalidade_padrão_A = "fale em portugues, expanda as ideias que lhe forem apresentadas, seja breve nas explicações, use emojis e finalize com uma pergunta ou ponderação"
        personalidade_padrão_B = "fale em portugues, discorde e apresente ideias contrárias ao que for falado pra você, seja breve nas suas explicações, use emojis e finalize com uma provocação"

        persona_A = Path("textos") / "persona" / "persona_A.txt"
        persona_B = Path("textos") / "persona" / "persona_B.txt"

        existe1 = persona_A.is_file()
        existe2 = persona_B.is_file()

        if existe1 and existe2:

            conteudo_A = persona_A.read_text('utf=8')
            conteudo_B = persona_B.read_text('utf=8')
            personalidades = []
            personalidades.extend([conteudo_A, conteudo_B])
            return personalidades
        
        elif existe1:

            persona_B.mkdir(parents=True, exist_ok=True)
            persona_B.write_text(personalidade_padrão_B)
        
        elif existe2:
            persona_A.mkdir(parents=True, exist_ok=True)
            persona_A.write_text(personalidade_padrão_A)


# Apenas verifica se existe o arquivo persona_chat.txt que será usado pra definir
# a personalidade do xat, se não existir, cria um com uma personalidade padrão.
def xat():

    personalidade_padrão = 'Você é uma inteligência artificial especializada em fornecer respostas úteis, claras e objetivas. Sempre responda com precisão, evite redundâncias e mantenha o foco na pergunta. Use linguagem simples, mas técnica quando necessário.'
    persona_xat = Path("textos/persona") / "persona_chat.txt"
    

    if persona_xat.is_file():
        arquivo = persona_xat.read_text('utf-8')
        return arquivo
    else:
        persona_xat.parent.mkdir(parents=True, exist_ok=True)
        persona_xat.write_text(personalidade_padrão, encoding='utf-8')
        
        arquivo = persona_xat.read_text('utf-8')
        return arquivo


    
