from translate import Translator

while True:
    def traduzir_mensagem(lang_origem, lang_final, mensagem):
        tradutor = Translator(from_lang=lang_origem, to_lang=lang_final)

        traducao = tradutor.translate(mensagem)

        print(traducao)


    lang_origem_e_lang_final = ['Linguagem de origem: ', 'Linguagem a traduzir: ']

    def menu():

        i = 0
        linguagens = []

        for i in range(2):
            print('------------------------------------------------')
            print('|          ESCOLHA UMA DAS LINGUAGENS          |')
            print('| [ES] Espanhol | [PT] Português | [EN] Inglês |')
            print('------------------------------------------------')
            print()

            linguagem = input(lang_origem_e_lang_final[i]).upper()

            while linguagem not in ['EN', 'PT', 'ES']:
                print("Digite um linguagem válida")
                linguagem = input(lang_origem_e_lang_final[i]).upper()

            linguagens.append(linguagem)

        return linguagens


    lang_usario = menu()

    mensagem_usuario = input("Digite o que deseja traduzir: ")

    traduzir = traduzir_mensagem(lang_usario[0], lang_usario[1], mensagem_usuario)

    # Não continua o código
    continuar = input('Deseja continuar a traduzir?').lower()
    nao_continua = ['nao', 'n', 'não']

    while True:
        if continuar in nao_continua:
            print('Obrigado, volte sempre!')
            break
        elif continuar in ['sim', 's', 'ss']:
            break
        else:
            print('Digite uma ação válida')
            continuar = input('Deseja continuar a traduzir? ')

    if continuar in nao_continua:
        break