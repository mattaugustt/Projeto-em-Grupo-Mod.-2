### Módulo 2 – Quero os dados na minha mesa. ###
#integrantes:
#Angélica Monteiro Correa
#Matheus Augusto de Souza
#Rodrigo de Souza Valim
#Vitor Hugo Almeida de Moura


import csv  # import da biblioteca que irá editar um arquivo csv
from datetime import datetime as dt  # biblioteca que fornece data e hora
from os import system  # biblioteca para manipular o cmd
from time import sleep


class Entrevista:  # criação da classe Entrevista
    def __init__(self):  # construtor para iniciar as variaveis
        #abertura do arquivo
        arquivo = open("saída.csv", "a", newline="", encoding="utf-8")
        #cabeçalho
        header = ['idade', 'faixa', 'genero', 'r1', 'r2', 'r3', 'r4', 'data']
        # criar um escritor de CSV
        w = csv.writer(arquivo)
        # escrever o cabeçalho no arquivo CSV
        w.writerow(header)

        self.idade = 1
        while (self.idade != 00):
            self.idade = int(input('Insira a idade do entrevistado (00 para encerrar o programa): '))
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
                self.gen = input('Insira o gênero do entrevistado: ').upper()
                sleep(0.5)
                system('cls')
                
                lista = ['A', 'B', 'C', 'D', 'E']
                
                lista1 = ['A) Shonen (Naruto, Dragon Ball...)', 'B) Shoujo (Sailor Moon, Colégio Ouran Host Club...)',
                          'C) Seinen (Monster, Berserk)', 'D) Josei (Usagi Drop)', 'E) Não sei']
                dic1 = {'A' : 'Shonen', 'B' : 'Shoujo', 'C' : 'Seinen', 'D' : 'Josei', 'E' : 'Não sabe'}
                
                lista2 = ['A) Ufotable (Franquia Fate, Kimetsu no Yaiba)', 'B) Toei (One Piece, Dragon Ball...)',
                          'C) Bones (Fumetal Alchimist: Brotherhood, Boku no Hero Academia...)',
                          'D) Pierrot (Naruto, Bleach)', 'E) Não sei']
                dic2 = {'A' : 'Ufotable', 'B' : 'Toei', 'C' : 'Bones', 'D' : 'Pierrot', 'E' : 'Não sabe'}
                
                lista3 = ['A) Sim', 'B) Não', 'C) Não sei']
                dic3 = {'A' : 'Sim', 'B' : 'Não', 'C' : 'Não sabe'}
                
                lista4 = ['A) TV', 'B) Sites', 'C) Streamings', 'D) Não sei']
                dic4 = {'A' : 'TV', 'B' : 'Sites', 'C' : 'Streamings', 'D' : 'Não sabe'}
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
                    self.r1 = input('Insira a primeira resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r1 in lista:
                        indice = lista.index(self.r1)
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
                    for i in lista2:
                        print(i)
                    print('')
                    self.r2 = input('Insira a segunda resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r2 in lista:
                        indice = lista.index(self.r2)
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
                    for i in lista3:
                        print(i)
                    print('')
                    self.r3 = input('Insira a terceira resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r3 in lista:
                        indice = lista.index(self.r3)
                        break
                    else:
                        print('')
                        print('***-_Resposta inválida!_-***')
                        sleep(1)
                        system('cls')
                    
                system('cls')
                while (True):
                    print('''    ##################################
    #           Pergunta 4           #
    ##################################'''
                          )
                    print('')
                    print('Por onde você costuma assistir animes?')
                    print('')
                    for i in lista4:
                        print(i)
                    print('')
                    self.r4 = input('Insira a quarta resposta do entrevistado: ').upper()
                    sleep(0.5)
                    if self.r4 in lista:
                        indice = lista.index(self.r4)
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


                infos = [self.idade, self.faixa, self.gen, dic1[self.r1], dic2[self.r2], dic3[self.r3], dic4[self.r4], self.data]            
                
                # escrever as infos no arquivo CSV
                w.writerow(infos)
                

                lista2 = ['Ficha do entrevistado:', '', f'Idade: {self.idade}', f'Faixa etária: {self.faixa}',
                          f'Genêro: {self.gen}', '', f'Resposta 1: {self.r1}', f'Resposta 2: {self.r2}',
                          f'Resposta 3: {self.r3}', f'Resposta 4: {self.r4}', '', f'Data: {self.data}']

                for i in lista2:
                    print(i)
                print('')
                p = input('Aperte enter para continuar\n')
                system('cls')
        arquivo.close()


