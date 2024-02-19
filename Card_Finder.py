from PIL import Image
import os

banco_de_dados_de_monstros = [
    {"nome": "Dark Magician", "tipo": "spellcaster", "atributo": "dark", "ataque": 2500, "defesa": 2100, "imagem": "dark_magician.png"},
    {"nome": "Blue-Eyes White Dragon", "tipo": "dragon", "atributo": "light", "ataque": 3000, "defesa": 2500, "imagem": "blue-eyes white dragon"},
    {"nome": "Red-Eyes Black Dragon", "tipo": "dragon", "atributo": "dark", "ataque": 2400, "defesa": 2000, "image": "red-eyes black dragon"},
    {"nome": "Flame Swordsman", "tipo": "warrior", "atributo": "fire", "ataque": 1800, "defesa": 1600, "imagem": "flame swordsman"},
    {"nome": "Kuriboh", "tipo": "fiend", "atributo": "dark", "ataque": 300, "defesa": 200},
    {"nome": "Gaia the Fierce Knight", "tipo": "warrior", "atributo": "earth", "ataque": 2300, "defesa": 2100, "imagem": "gaia the fierce knight"},
    {"nome": "Celtic Guardian", "tipo": "warrior", "atributo": "earth", "ataque": 1400, "defesa": 1200, "imagem": "celtic guardian"},
    {"nome": "Summoned Skull", "tipo": "fiend", "atributo": "dark", "ataque": 2500, "defesa": 1200, "imagem": "summoned skull"},
    {"nome": "Gazelle The King Of Mythical Beasts", "tipo": "beast", "atributo": "earth", "ataque": 1500, "defesa": 1200, "imagem": "gazelle the king of mythical beasts"},
    {"nome": "Theinen The Great Sphinx", "tipo": "beast", "atributo": "light", "ataque": 3500, "defesa": 3000},
    {"nome": "Right Arm of Forbidden One", "tipo": "spellcaster", "atributo": "dark", "ataque": 200, "defesa": 300},
    {"nome": "left Arm of Forbidden One", "tipo": "spellcaster", "atributo": "dark", "ataque": 200, "defesa": 300},
    {"nome": "Right leg of Forbidden One", "tipo": "spellcaster", "atributo": "dark", "ataque": 200, "defesa": 300},
    {"nome": "left leg of Forbidden One", "tipo": "spellcaster", "atributo": "dark", "ataque": 200, "defesa": 300},
    {"nome": "Exodia The Forbidden One", "tipo": "spellcaster", "atributo": "dark", "ataque": 1000, "defesa": 1000, "imagem": "exodia the forbidden one"},
]

banco_de_dados_de_magias_e_armadilhas = [
    {"nome": "Polymerization", "tipo": "magic", "imagem": "polymerization"},
    {"nome": "Swords of Revealing Light", "tipo": "magic", "imagem": "swords of revealing light"},
    {"nome": "Premature Burial", "tipo": "magic", "imagem": "premature Burial"},
    {"nome": "Return of Dragon Lords", "tipo": "magic", "imagem": "return of dragon lords"},
    {"nome": "Monster Reborn", "tipo": "magic", "imagem": "monster reborn"},
    {"nome": "Mirror Force", "tipo": "trap", "imagem": "monster reb4orn"},
    {"nome": "Metalmorph", "tipo": "trap", "imagem": "metalmorph"},
    {"nome": "Dust Tornado", "tipo": "trap", "imagem": "dust tornado"},
    {"nome": "Two-Pronged Attack", "tipo": "trap", "imagem": "two-pronged attack"},
    {"nome": "Trap Hole", "tipo": "trap", "imagem": "trap hole"},
]

diretorio_imagens = r"D:\Nova pasta"

atributos_validos = ["dark", "light", "fire", "earth"]
tipos_validos = ["dragon", "spellcaster", "warrior", "fiend", "beast"]

def procurar_monstros(tipo=None, atributo=None, nome=None, ataque=None, defesa=None):
    resultados = []
    for monstro in banco_de_dados_de_monstros:
        if (tipo is None or monstro["tipo"] == tipo) and (atributo is None or monstro["atributo"] == atributo) and (nome is None or monstro["nome"] == nome):
            if ataque is not None and monstro["ataque"] != ataque:
                continue
            if defesa is not None and monstro["defesa"] != defesa:
                continue
            resultados.append(monstro)
    return resultados

def obter_caminho_imagem(nome_monstro):
    return os.path.join(diretorio_imagens, f"{nome_monstro}.png")

def obter_caminho_imagem(resultados):
    return os.path.join(diretorio_imagens, f"{resultados}.png")

def procurar_magias_e_armadilhas(tipo=None, nome=None):
    resultados = []
    for carta in banco_de_dados_de_magias_e_armadilhas:
        if (tipo is None or carta["tipo"] == tipo) and (nome is None or carta["nome"] == nome):
            resultados.append(carta)
    return resultados

while True:
    print("Opções:")
    print("1. Procurar monstros por tipo e atributo")
    print("2. Procurar monstros por tipo")
    print("3. Procurar monstros por atributo")
    print("4. Procurar monstro por nome")
    print("5. Procurar monstros por ataque e defesa")
    print("6. Procurar magias e armadilhas por nome")
    print("7. Sair")

    opcao = input("Escolha uma opção (1 a 7): ")

    if opcao == "1":
        tipo = input("Informe o tipo do monstro: ")
        atributo = input("Informe o atributo do monstro: ")
        if tipo in tipos_validos and atributo in atributos_validos:
            resultados = procurar_monstros(tipo, atributo)
            if resultados:
                print("Monstros encontrados:")
                for monstro in resultados:
                    print(monstro["nome"])
            else:
                print("Nenhum monstro encontrado.")
        else:
            print("Tipo ou atributo inválido. Tente novamente.")
    elif opcao == "2":
        tipo = input("Informe o tipo do monstro: ")
        if tipo in tipos_validos:
            resultados = procurar_monstros(tipo=tipo)
            if resultados:
                print("Monstros encontrados:")
                for monstro in resultados:
                    print(monstro["nome"])
            else:
                print("Nenhum monstro encontrado.")
        else:
            print("Tipo inválido. Tente novamente.")
    elif opcao == "3":
        atributo = input("Informe o atributo do monstro: ")
        if atributo in atributos_validos:
            resultados = procurar_monstros(atributo=atributo)
            if resultados:
                print("Monstros encontrados:")
                for monstro in resultados:
                    print(monstro["nome"])
            else:
                print("Nenhum monstro encontrado.")
        else:
            print("Atributo inválido. Tente novamente.")
    elif opcao == "4":
        nome = input("Informe o nome do monstro: ")
        resultados = procurar_monstros(nome=nome)
        if resultados:
            monstro_encontrado = resultados[0]
            print(f"Monstro encontrado:")
            print(f"Nome: {monstro_encontrado['nome']}")
            print(f"Tipo: {monstro_encontrado['tipo']}")
            print(f"Atributo: {monstro_encontrado['atributo']}")
            print(f"Ataque: {monstro_encontrado['ataque']}")
            print(f"Defesa: {monstro_encontrado['defesa']}")

            caminho_imagem = obter_caminho_imagem(monstro_encontrado['nome'])
            print(f"Caminho da imagem: {caminho_imagem}")

            try:
                imagem = Image.open(caminho_imagem)
                imagem.show()
            except Exception as e:
                print(f"Erro ao abrir a imagem: {e}")
        else:
            print(f"O monstro '{nome}' não foi encontrado no banco de dados.")
    elif opcao == "5":
        ataque = input("Informe o número de ataque: ")
        defesa = input("Informe o número de defesa: ")
        resultados = procurar_monstros(ataque=int(ataque), defesa=int(defesa))
        if resultados:
            print("Monstros encontrados:")
            for monstro in resultados:
                print(monstro["nome"])
        else:
            print("Nenhum monstro encontrado.")
    elif opcao == "6":
        nome = input("Informe o nome da magia ou armadilha: ")
        resultados = procurar_magias_e_armadilhas(nome=nome)
        if resultados:
            print(f"Magia ou armadilha encontrada:")
            print(f"Nome: {resultados[0]['nome']}")
            print(f"Tipo: {resultados[0]['tipo']}")
            caminho_imagem = obter_caminho_imagem(resultados[0]['nome'])
           
        try:
            imagem = Image.open(caminho_imagem)
            imagem.show()
        except Exception as e:
            print(f"Erro ao abrir a imagem: {e}")
        else:
            print(f"A magia ou armadilha '{nome}' não foi encontrada no banco de dados.")
    elif opcao == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        
