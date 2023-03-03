### Módulo 2 – Quero os dados na minha mesa. ###
#integrantes:
#Angélica Monteiro Correa
#Matheus Augusto de Souza
#Rodrigo de Souza Valim
#Victor Hugo Almeida de Moura

import csv # import da biblioteca que irá editar um arquivo csv
from datetime import datetime as dt # biblioteca que fornece data e hora
from os import system # biblioteca para manipular o cmd
from time import sleep 

class Entrevista: # criação da classe Entrevista
    def __init__(self): # construtor para iniciar as variaveis
        idade = 1
        arquivo = open("saída.csv", "a", newline="", encoding="utf-8")   #abre/cria o arquivo para inserir os dados
        w = csv.writer(arquivo)                
        w.writerow(['idade', 'genero', 'r1', 'r2', 'r3', 'r4', 'data'])
        
        while (idade != 00):
            
            dados = []
            idade = int(input ('Insira a idade do entrevistado (00 para encerrar o programa): '))
            sleep(1)
            print('')

            if idade == 00:
              break
            
            gen = input('Insira o gênero do entrevistado: ')
            sleep(1)
            print('')
            r1 = input ('''1 - Qual o gênero de anime favorito do entrevistado?
            exs.:
            Shonen (Naruto, Dragon Ball), 
            Shoujo (Sailor Moon, Colégio Ouran Host Club),
            Seinen (Monster, Berserk)
            Josei (Usagi Drop). \n''')
            sleep(1)
            print('')
            r2 = input (''' Qual a produtora de anime favorita do entrevistado? 
            exs.:
            Ufotable - Franquia Fate, Kimetsu no Yaiba,
            Trigger - Little Witch Academia,
            Bones - Fullmetal Alchemist: Brotherhood, Boku no Hero Academia
            CloverWorks - The Promised Neverland,
            Wit Studio - Shingeki No Kyojin,
            Mappa - Jujutsu Kaisen, The God of High School,
            Toei - One Piece, Dragon Ball,
            Pierrot - Naruto,
            Production I.G - Kuroko no Basket. \n''')
            sleep(1)
            print('')
            r3 = input ('Há algum mangá que o entrevistado gostaria que fosse adaptado (ou re-adaptado) para anime? Se sim, qual?\n')
            sleep(1)
            print('')
            r4 = input ('De qual forma o entrevistado costuma assistir anime? \n(exs.: canais de TV, sites, plataforma de streaming etc)\n')
            sleep(1)
            print('')
            data = dt.now().strftime('%Y-%m-%d %H:%M:%S')
            sleep(1)
            print('')
                
            dados.append(idade)
            dados.append(gen)
            dados.append(r1)
            dados.append(r2)
            dados.append(r3)
            dados.append(r4)
            dados.append(data)
                
            w.writerow(dados)  #adiciona os dados
            system('cls')  #limpa o terminal a cada iteração.

        arquivo.close()  #fecha o arquivo
