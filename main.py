from config.bd import criar_conexao
from servicos.Listagem import *

print ("Bem vindos a loja de jogos!")
while True:
    print("1- Listar jogos")
    print("2- Buscar por letra")
    opc = int(input("o que gostaria de fazer: ") )

    match opc:
        case 1:
            print ("Lista de jogos Disponíveis: \n")
            listagem()
        case 2:
            letra = input("Digite a letra que tenha no título ou subtítulo: ").upper()
            buscaLetra(letra)