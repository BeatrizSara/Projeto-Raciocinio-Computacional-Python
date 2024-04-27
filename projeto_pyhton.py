""" 
Analise e Desenvolvimento de sistemas - ADS
Beatriz Sara dos Santos
"""

import os # importando para usar função de limpar o terminal
import time
import msvcrt


def mostrar_menu_principal():
    print("==== Menu Principal ==== ")
    print("1. Estudante")
    print("2. Disciplina")
    print("3. Professor")
    print("4. Turma")
    print("5. Matricula")
    print("0. Sair do Sistema")
    # Coleta da opção 1 escolida pelo usuário
    return int(input("Informe uma opção: "))


def mostrar_menu_operacoes():
    print("== Menu de Operações ==")
    print("1. Incluir")
    print("2. Listar")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")
    # Coleta da opção da oepração selecionada do usuario
    codigo_selecionado = int(input("Informe uma opção válida: "))
    return codigo_selecionado


# Vai imprimir o nome da opcao selecionada no menu principal
def exibir_selecionado_menu_principal(opcao_menu_principal): 
    if opcao_menu_principal == 1:
        print("Opção Estudante")
    elif opcao_menu_principal == 2:
        print("Opção Disciplina")
    elif opcao_menu_principal == 3:
        print("Opção Professor")
    elif opcao_menu_principal == 4:
        print("Opção Turma")
    else:
        print("Opção Matrícula")
        

# Recebe qual foi a operacao selecionada e a lista respectiva do menu principal        
def executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, listas): 
    if opcao_operacao_selecionada == 1:
        incluir(opcao_menu_principal, listas)
    elif opcao_operacao_selecionada == 2:
        listar(listas)
    elif opcao_operacao_selecionada == 3:
        alterar(opcao_menu_principal, listas)
    elif opcao_operacao_selecionada == 4:
        excluir(opcao_menu_principal, listas)
        
# Recebe qual foi a operacao selecionada e dados(que é a lista) do menu principal
def incluir(opcao_menu_principal, dados):
    print("Opcao do menu operações selecionado: Incluir")
    if opcao_menu_principal == 1:
        codigo_aluno = int(input("Digite o código: "))
        nome = str(input("Insira o nome do Estudante: "))
        cpf = input("Digite o CPF: ")
        estudante_dicionario = {"cod_estudante": codigo_aluno, "nome_estudante":nome,"cpf_estudante": cpf }
        dados.append(estudante_dicionario)# Nao sera mais de uma string nome, mas sim o append do dicionario
        
    elif opcao_menu_principal == 2:
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
    elif opcao_menu_principal == 3:
        codigo_professor = int(input("Digite o código do professor: "))
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
    elif opcao_menu_principal  == 4:
        codigo_turma = int(input("Digite o código da turma: "))
        print("Em DESENVOLVIMENTO!")
        time.sleep(3)
    else:
        codigo_matricula = int(input("Digite o código da matrícula: "))
        print("Em DESENVOLVIMENTO!")
        time.sleep(3)
        
# Mostra os dados da lsita passado pelo def anterior          
def listar(dados):
    print("Opcao do menu operações selecionado: Listar")
    if len(dados) > 0:
        for dado in dados:
            print(dado)
    else:
        print("Não há dados cadastrados")
            
    print("Pressione qualquer tecla para continuar")
    msvcrt.getch() # Pausa o sistema até que uma  tecla seja pressionada
    
# Altera o valor do dicionario 
def alterar(opcao_menu_principal, listas):
    print("Opcao do menu operações selecionado: Alterar")
    codigo = int(input("Qual código deseja alterar: "))
    
    if opcao_menu_principal == 1:
        alterar_estudante = None
        
        for estudante_dicionario in listas:
            if estudante_dicionario["cod_estudante"] == codigo:
                alterar_estudante = estudante_dicionario
                break
        
        if alterar_estudante is None: # Caso o código nao seja localizado para realizar alterações
            print(f"Não foi localizado o código {codigo} do estudante na lista")
        
        else: # Caso o código seja localizado para realizar alterações
            alterar_estudante["cod_estudante"] = int(input("Informe o novo código: "))
            alterar_estudante["nome_estudante"] = input("Informe o novo nome: ")
            alterar_estudante["cpf_estudante"] = input("Informe o novo CPF: ")
            print("Código do estudante alterado com sucesso!")
            
        for estudante in listas:
            print(estudante)
    
    elif opcao_menu_principal == 2:
        alterar_disciplina = None
        print("Em DESENVOLVIMENTO!")
        time.sleep(3)  
        
    elif opcao_menu_principal == 3:
        alterar_professor = None
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
        
    elif opcao_menu_principal  == 4:
        alterar_turma = None
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
        
    else:
        alterar_matricula = None
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 

    print("Pressione qualquer tecla para limpar o terminal e continuar")
    msvcrt.getch() # comando para continuar o programa após preessionar qualquer tecla, como Enter por exemplo
    
# Realiza a exclusão do código selecionado
def excluir(opcao_menu_principal, listas):
    print("Opcao do menu operações selecionado: Excluir")
    excluir_codigo = int(input("Qual código deseja excluir: "))
    
    if opcao_menu_principal == 1:
        remover_estudante = None # Funcionalidade para exluir código
        
        for estudante_dicionario in listas: # For, vai pesquisar o estudante na lista de estudantes
            if estudante_dicionario["cod_estudante"] == excluir_codigo: # Se o estudante é localizado pelo código solicitado,
                remover_estudante = estudante_dicionario                # é armazenado todo o dicionario dentro de uma variavel temporaria - remover_estudante
                break
        if remover_estudante is None: # Se o estudante não foi encontrado
            print(f"Não foi localizado o código {excluir_codigo} do estudante na lista")
        else:
            listas.remove(remover_estudante)
            print("Código do estudante removido com sucesso!")
            
    elif opcao_menu_principal == 2:
        remover_disciplina = None # Funcionalidade para exluir código
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
        
    elif opcao_menu_principal == 3:
        remover_professor = None # Funcionalidade para exluir código
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
        
    elif opcao_menu_principal == 4:
        remover_turma = None # Funcionalidade para exluir código
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 
        
    else:
        remover_matricula = None # Funcionalidade para exluir código
        print("Em DESENVOLVIMENTO!")
        time.sleep(3) 

    print(listas)
        
    print("Pressione qualquer tecla para limpar o terminal e continuar")
    msvcrt.getch() # comando para continuar o programa após preessionar qualquer tecla, como Enter por exemplo


lista_estudantes = []
lista_disciplinas = []
lista_professores = []
lista_turmas = []
lista_matriculas = []

# Código principal
while True: # Estrutura de condição while repetindo enquanto as opções forem verdadeiras ou houver um break
    os.system("cls") # Função para limpar o terminal
    opcao_menu_principal = mostrar_menu_principal() # o resultado digitado pelo usuário sera guardado dentro dessa variavel 'opcao_menu_principal'
    
    # Verificação da opcao_menu_principal informada pelo usuário
    if opcao_menu_principal == 1 or opcao_menu_principal == 2 or opcao_menu_principal == 3 or opcao_menu_principal == 4 or opcao_menu_principal == 5:
        while True: # Estrutura de condição while caso as opções sejam verdadeiras
            os.system("cls") # Função para limpar o terminal
            print("Escolheu a opção {}".format(opcao_menu_principal))
            exibir_selecionado_menu_principal(opcao_menu_principal)
            # Possibilidades de opcao_menu_principal selecionada pelo usuário
            opcao_operacao_selecionada = mostrar_menu_operacoes()
            
            if opcao_operacao_selecionada == 1 or opcao_operacao_selecionada == 2 or opcao_operacao_selecionada == 3 or opcao_operacao_selecionada == 4:
                os.system("cls")
                print("Escolheu a opção {}".format(opcao_operacao_selecionada))
                
                # ESTUDANTES
                if opcao_menu_principal == 1:
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, lista_estudantes)    

                # DISCIPLINA
                elif opcao_menu_principal == 2:
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, lista_disciplinas)
                
                # PROFESSOR        
                elif opcao_menu_principal == 3:
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, lista_professores)
                
                # TURMA        
                elif opcao_menu_principal == 4:
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, lista_turmas)
                
                # MATRICULA        
                elif opcao_menu_principal == 5:
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, lista_matriculas)
                        
            elif opcao_operacao_selecionada == 5:
                print("Voltando ao menu principal")
                print("Limpando o terminal em 5 segundos ")
                time.sleep(5) 
                break
            else: 
                print("Solicitou uma opção INVÁLIDA")

    # Verificação da opção "sair do sistema" para encerrar o programa
    elif opcao_menu_principal == 0:
        print("Opção selecionada: Sair do sistema")
        time.sleep(3)        
        break # Sinalização para sair do loop
    
    # Informar opção Inválida ao usuário
    else:
        print("Opção INVÁLIDA")
        print("Tente novamente")
        time.sleep(3) # Pausa de 3 seg para execução do código