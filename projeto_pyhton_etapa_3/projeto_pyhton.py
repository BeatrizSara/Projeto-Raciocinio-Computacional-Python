""" 
Analise e Desenvolvimento de sistemas - ADS
Beatriz Sara dos Santos
"""

import os # importando para usar função de limpar o terminal
import time

nomes_estudantes = []

while True: # Estrutura de condição while repetindo enquanto as opções forem verdadeiras ou houver um break
    os.system("cls") # Função para limpar o terminal
    # Menu principal 
    print("==== Menu Principal ==== ")
    print("1. Estudante")
    print("2. Disciplina")
    print("3. Professor")
    print("4. Turma")
    print("5. Matricula")
    print("0. Sair do Sistema")
    # Coleta da opção 1 escolida pelo usuário
    opcao = int(input("Informe uma opção: "))

    # Verificação da opcao informada pelo usuário
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        while True: # Estrutura de condição while caso as opções sejam verdadeiras
            os.system("cls") # Função para limpar o terminal
            print("Escolheu a opção {}".format(opcao))
            # Possibilidades de opcao selecionada pelo usuário
            if opcao == 1:             

                print("Opção Estudante")
                print("== Menu Operações ==")
                print("1. Incluir")
                print("2. Listar")
                print("3. Alterar")
                print("4. Excluir")
                print("5. Voltar ao menu anterior")
                # Coleta da opção da oepração selecionada do usuario
                opcao_2 = int(input("Informe uma opção válida: "))
                os.system("cls")
                print("Escolheu a opção {}".format(opcao_2))
                
                # Verificação da opcao informada pelo usuário
                if opcao_2 == 1 or opcao_2 == 2 or opcao_2 == 3 or opcao_2 == 4:
                    # Possibilidades de opcao selecionada pelo usuário
                    if opcao_2 == 1:
                        print("Opcao do menu operações selecionado: Incluir")
                        
                        nome = str(input("Insira o nome do Estudante: "))
                        nomes_estudantes.append(nome)

                    elif opcao_2 == 2:
                        print("Opcao do menu operações selecionado: Listar")
                        
                        if len(nomes_estudantes) > 0:
                            for nome in nomes_estudantes:
                                print(nome)

                        else:
                            print("Não há estudantes cadastrados")
                        
                        time.sleep(5) # Pausa de 5 seg para execução do código
                            
                    elif opcao_2 == 3:
                        print("Opcao do menu operações selecionado: Alterar")
                        print("EM DESENVOLVIMENTO")
                        print("Limpando o terminal em 5 seg")
                        time.sleep(5) # Pausa de 5 seg para execução do código
                    elif opcao_2 == 4:
                        print("Opcao do menu operações selecionado: Excluir")
                        print("EM DESENVOLVIMENTO")
                        print("Limpando o terminal em 5 seg")
                        time.sleep(5) # Pausa de 5 seg para execução do código
                # Condição selecionada pelo usuário para parar o loop do menu operações e retornar ao menu principal
                elif opcao_2 == 5:
                    print("Voltando ao menu principal")
                    print("Limpando o terminal em 5 seg")
                    time.sleep(5) # Pausa de 5 seg para execução do código
                    break
        
                else: 
                    print("Solicitou uma opção INVÁLIDA")
                
            elif opcao == 2:
                print("Opção Disciplina")
                print("== EM DESENVOLVIMENTO ==")
                time.sleep(5) # Pausa de 5 seg para execução do código
                break
            elif opcao == 3:
                print("Opção Professor")
                print("== EM DESENVOLVIMENTO ==")
                time.sleep(5) # Pausa de 5 seg para execução do código
                break
            elif opcao == 4:
                print("Opção Turma")
                print("== EM DESENVOLVIMENTO ==")
                time.sleep(5) # Pausa de 5 seg para execução do código
                break
            elif opcao == 5:
                print("Opção Matrícula")
                print("== EM DESENVOLVIMENTO ==")
                time.sleep(5) # Pausa de 5 seg para execução do código
                break

            
    # Verificação da opção "sair do sistema" para encerrar o programa
    elif opcao == 0:
        print("Opção selecionada: Sair do sistema")
        time.sleep(3) # Pausa de 3 seg para execução do código        
        break # Sinalização para sair do loop
    # Informar opção Inválida ao usuário
    else:
        print("Opção INVÁLIDA")
        print("Tente novamente")
        time.sleep(3) # Pausa de 3 seg para execução do código