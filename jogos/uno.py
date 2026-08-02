import random


# Lista de jogadores da partida atual
jogadores = []


# Cartas de cada jogador
cartas_jogadores = {}


# Carta que está na mesa
carta_atual = None


# Controle da vez do jogador
vez = 0



# Baralho básico UNO

baralho = [

    "🔴 1 Vermelho",
    "🔴 3 Vermelho",
    "🔴 5 Vermelho",

    "🔵 2 Azul",
    "🔵 Bloqueio Azul",
    "🔵 Inverter Azul",

    "🟢 4 Verde",
    "🟢 +2 Verde",

    "🟡 7 Amarelo",
    "🟡 Inverter Amarelo",

    "🌈 Coringa",
    "🌈 +4"

]



# Criar uma nova partida

def criar_partida():

    global jogadores
    global cartas_jogadores
    global carta_atual
    global vez


    jogadores = []

    cartas_jogadores = {}

    carta_atual = None

    vez = 0




# Adicionar jogador

def entrar_jogador(nome):

    if nome not in jogadores:

        jogadores.append(nome)

        cartas_jogadores[nome] = []

        return True


    return False





# Iniciar jogo e distribuir cartas

def iniciar_uno():

    global carta_atual


    if len(jogadores) < 2:

        return False


    for jogador in jogadores:

        cartas_jogadores[jogador] = random.sample(
            baralho,
            7
        )


    carta_atual = random.choice(
        baralho
    )


    return True





# Mostrar status da partida

def status_uno():


    if not jogadores:

        return """

🃏 UNO KIARA GLAM

Nenhuma partida ativa.

Use /uno para criar uma partida.
"""



    texto = """

🃏 UNO KIARA GLAM 🌊


Carta atual:

""" + str(carta_atual) + "\n\n"



    texto += "Jogadores:\n\n"



    for jogador in jogadores:


        quantidade = len(
            cartas_jogadores.get(
                jogador,
                []
            )
        )


        texto += (

            f"🌹 {j
