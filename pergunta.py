from pathlib import Path

def assunto():

    print("\n\nVocê mesmo quer definir o tema do debate ou quer usar um arquivo de texto " \
    "como referência? \n" \
    "Caso queia usar um arquivo de texto, cole todo o texto no arquivo tema.txt " \
    "no diretório textos.\n " \
    "Digite 1 ou 2:\n" \
    "1) Definir tema do debate\n" \
    "2) Usar arquivo de texto como base\n")
    
    while True:

        alternativa = input(": ")

        if alternativa == '1':

            tema = input("Qual o tema do debate? ")
            return tema
            break

        elif alternativa == '2':

            try:
                procurar_arquivo = Path("textos") / "tema.txt"
                tema = procurar_arquivo.read_text(encoding='utf-8')
                return tema
                break

            except FileNotFoundError:
                print("\n Arquivo não encontrado. Por favor crie um arquivo" \
                " tema.txt no diretório textos ")

        else:
            print("digite uma alternativa válida")