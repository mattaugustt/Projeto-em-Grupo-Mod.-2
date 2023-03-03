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
        arquivo = open("saída.csv", "a", newline="", encoding="utf-8")    #abre o arquivo para adicionar os dados
        self.idade = 1
        while (self.idade != 00):
            self.idade = int(input ('Insira a idade do entrevistado (00 para encerrar o programa): '))
            sleep(0.5)
            if self.idade < 12:
                self.faixa = 'Criança'
            if self.idade >= 12 and self.idade <= 21:
                self.faixa = 'Adolescente'
            if self.idade > 21:
                self.faixa = 'Adulto'
            print('')
            if self.idade == 00:
                system('cls')
                break
            else:
                self.gen = input ('Insira o gênero do entrevistado: ').upper()
                sleep(0.5)
                system('cls')
                lista3 = ['A', 'B', 'C', 'D', 'E']
                lista1 = ['A) Shonen (Naruto, Dragon Ball...)', 'B) Shoujo (Sailor Moon, Colégio Ouran Host Club...)', 'C) Seinen (Monster, Beserk)', 'D) Josei (Usagi Drop)', 'E) Não sei']
                lista4 = ['A) Ufotable (Franquia Fate, Kimetsu no Yaiba)', 'B) Toei (One Piece, Dragon Ball...)', 'C) Bones (Fumetal Alchimist: Brotherhood, Boku no Hero Academia...)', 'D) Pierrot (Naruto, Bleach)', 'E) Não sei']
                lista5 = ['A) Sim', 'B) Não','C) Não sei']
                lista6 = ['A) TV', 'B) Sites', 'C) Streamings', 'D) Não sei']
                while (True):
                    print(
                        '''##################################
#           Pergunta 1           #
##################################'''
)
                    print('')
                    print('Qual seu gênero de anime favorito?')
                    print('')
                    for i in lista1:
                        print(i)
                    print('')
                    self.r1 = input ('Insira a primeira resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r1 in lista3:
                        break
                    else:
                        print('')
                        print('***-_Resposta inválida!_-***')
                        sleep(1)
                    system('cls')
                system('cls')
                while (True):
                    print('''    ##################################
    #           Pergunta 2           #
    ##################################'''
    )
                    print('')
                    print('Qual sua produtora de anime favorita?')
                    print('')
                    for i in lista4:
                        print(i)
                    print('')
                    self.r2 = input ('Insira a segunda resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r2 in lista3:
                        break
                    else:
                        print('')
                        print('***-_Resposta inválida!_-***')
                        sleep(1)
                    system('cls')
                system('cls')
                while (True):
                    print('''    ##################################
    #           Pergunta 3           #
    ##################################'''
    )
                    print('')
                    print('Há algum mangá que o entrevistado gostaria que fosse adaptado (ou re-adaptado) para anime?')
                    print('')
                    for i in lista5:
                        print(i)
                    print('')
                    self.r3 = input ('Insira a terceira resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r3 in lista3:
                        break
                    else:
                        print('')
                        print('***-_Resposta inválida!_-***')
                        sleep(1)
                        system('cls')
                system('cls')
                while(True):
                    print('''    ##################################
    #           Pergunta 4           #
    ##################################'''
    )
                    print('')
                    print('Por onde você costuma assistir animes?')
                    print('')
                    for i in lista6:
                        print(i)
                    print('')
                    self.r4 = input ('Insira a quarta resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r4 in lista3:
                            break
                    else:
                        print('')
                        print('***-_Resposta inválida!_-***')
                        sleep(1)
                        system('cls')
                system('cls')
                
                print('')
                self.data = dt.now().strftime('%d-%m-%Y %H:%M:%S')
                system('cls')

                w = csv.writer(arquivo)
                cabecalho = ['idade', 'faixa', 'genero', 'r1', 'r2', 'r3', 'r4', 'data']
                writer = csv.DictWriter(arquivo, fieldnames = cabecalho)
                #writer.writeheader()
                writer.writerow({'idade':self.idade, 'faixa':self.faixa, 'genero':self.gen, 'r1':self.r1, 'r2':self.r2, 'r3':self.r3, 'r4':self.r4, 'data':self.data})

                lista2 = ['Ficha do entrevistado:','', f'Idade: {self.idade}', f'Faixa etária: {self.faixa}', f'Genêro: {self.gen}', '', f'Resposta 1: {self.r1}', f'Resposta 2: {self.r2}', f'Resposta 3: {self.r3}', f'Resposta 4: {self.r4}', '', f'Data: {self.data}']
 
                for i in lista2:
                    print(i)
                print('')
                p = input ('Aperte enter para continuar\n')
                system('cls')
        arquivo.close()    #fecha o arquivo
        
