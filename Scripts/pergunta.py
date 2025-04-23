from pathlib import Path

def assunto():

    print("\n\nVocê mesmo quer definir o tema do debate ou quer usar um arquivo de texto " \
    "como referência? \n" \
    "Caso queia usar um arquivo de texto, cole todo o texto no arquivo tema.txt " \
    "no diretório textos.\n " \
    "Digite 1,2 ou 3:\n" \
    "1) Definir tema do debate entre modelos \n" \
    "2) Usar arquivo de texto como base para debate entrem modelos \n" \
    "3) Debater você mesmo com o modelo " \
    "\n\n 📕 Você pode definir a personalidade dos modelos A,B e Chat no diretório\n" \
    "textos/persona/ nos arquivos persona_A, persona_B e persona_chat. \n Você pode ver referências de " \
    "personalidades no arquivo referências_personalidades.txt\n\n" )
    
    while True:

        alternativa = input(": ")
        assunto = []
        if alternativa == '1':

            tema = input("Qual o tema do debate? ")
            
            assunto.extend([tema, 'debate_entre_modelos'])
            return assunto

        elif alternativa == '2':

            try:
                procurar_arquivo = Path("textos") / "tema.txt"
                tema = procurar_arquivo.read_text(encoding='utf-8')
                assunto.extend([tema, 'debate_entre_modelos'])
                return assunto

            except FileNotFoundError:
                print("\n Arquivo não encontrado. Por favor crie um arquivo" \
                " tema.txt no diretório textos ")

        elif alternativa == '3':
            return 'conversar_com_modelo'

        else:
            print("digite uma alternativa válida")