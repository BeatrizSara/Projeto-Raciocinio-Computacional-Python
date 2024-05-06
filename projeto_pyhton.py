""" 
Analise e Desenvolvimento de sistemas - ADS
Beatriz Sara dos Santos
"""

import os # importando para usar função de limpar o terminal
import time
import msvcrt
import json

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
def executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados): 
    if opcao_operacao_selecionada == 1:
        incluir(opcao_menu_principal, dados)
    elif opcao_operacao_selecionada == 2:
        listar(dados)
    elif opcao_operacao_selecionada == 3:
        alterar(opcao_menu_principal, dados)
    elif opcao_operacao_selecionada == 4:
        excluir(opcao_menu_principal, dados)
        
# Recebe qual foi a operacao selecionada e dados(que é a lista) do menu principal
def incluir(opcao_menu_principal, lista_dados):
    print("Opcao do menu operações selecionado: Incluir")
    if opcao_menu_principal == 1:
        codigo_aluno = int(input("Digite o código: "))
        nome = str(input("Insira o nome do Estudante: "))
        cpf = input("Digite o CPF: ")
        estudante_dicionario = {"cod_estudante": codigo_aluno, "nome_estudante":nome,"cpf_estudante": cpf }
        lista_dados.append(estudante_dicionario)# Nao sera mais de uma string nome, mas sim o append do dicionario
        salvar_arquivo(lista_dados, arquivo_estudante)
        
        
    elif opcao_menu_principal == 2:
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        nome = str(input("Insira o nome da Disciplina: "))
        disciplina_dicionario = {"cod_disciplina":codigo_disciplina, "nome_disciplina":nome}
        lista_dados.append(disciplina_dicionario)
        salvar_arquivo(lista_dados, arquivo_disciplinas)
        
        
    elif opcao_menu_principal == 3:
        codigo_professor = int(input("Digite o código do professor: "))
        nome = str(input("Insira o nome do Professor: "))
        cpf = input("Digite o CPF: ")
        professor_dicionario = {"cod_professor":codigo_professor, "nome_professor":nome}
        lista_dados.append(professor_dicionario)
        salvar_arquivo(lista_dados, arquivo_professores)
        
        
    elif opcao_menu_principal  == 4:
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_professor = int(input("Digite o código do professor: "))
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        turma_dicionario = {"cod_turma": codigo_turma, "cod_professor": codigo_turma, "cod_disciplina": codigo_disciplina}
        lista_dados.append(turma_dicionario)
        salvar_arquivo(lista_dados, arquivo_turmas)
        
        
    else:
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        matricula_dicionario = {"cod_turma": codigo_turma, "cod_estudante": codigo_estudante}
        lista_dados.append(matricula_dicionario)
        salvar_arquivo(lista_dados, arquivo_matriculas)

    
    print("Registro incluido com sucesso!")
    print("Pressione qualquer tecla para continuar")
    msvcrt.getch() # Pausa o sistema até que uma  tecla seja pressionada
        
# Mostra os dados da lsita passado pelo def anterior          
def listar(lista_dados):
    print("Opcao do menu operações selecionado: Listar")
    if len(lista_dados) > 0:
        for dado in lista_dados:
            print(dado)
    else:
        print("Não há dados cadastrados")
            
    print("Pressione qualquer tecla para continuar")
    msvcrt.getch() # Pausa o sistema até que uma  tecla seja pressionada
    
# Altera o valor do dicionario 
def alterar(opcao_menu_principal, lista_dados):
    print("Opcao do menu operações selecionado: Alterar")
    codigo_nao_encontrado = True
    
    if opcao_menu_principal == 1:
        alterar_estudante = None
        codigo = int(input("Qual código do estudante deseja alterar: "))
        
        for estudante_dicionario in lista_dados:
            if estudante_dicionario["cod_estudante"] == codigo:
                alterar_estudante = estudante_dicionario
                alterar_estudante["cod_estudante"] = int(input("Informe o novo código: "))
                alterar_estudante["nome_estudante"] = input("Informe o novo nome: ")
                alterar_estudante["cpf_estudante"] = input("Informe o novo CPF: ")
                salvar_arquivo(lista_dados, arquivo_estudante)
                print("Registro alterado com sucesso!")
                codigo_nao_encontrado = False
        
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {codigo} do estudante na lista")
    
    elif opcao_menu_principal == 2:
        alterar_disciplina = None
        codigo = int(input("Qual código da disciplina deseja alterar: "))
        for disciplina_dicionario in lista_dados:
            if disciplina_dicionario["cod_disciplina"] == codigo:
                alterar_disciplina = disciplina_dicionario
                alterar_disciplina["cod_disciplina"] = int(input("Informe novo código: "))
                alterar_disciplina["nome_disciplina"] = input("Informe a nova disciplina: ")
                salvar_arquivo(lista_dados, arquivo_disciplinas)
                codigo_nao_encontrado = False
        
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {codigo} da disciplina na lista")
        
    elif opcao_menu_principal == 3:
        alterar_professor = None
        codigo = int(input("Qual código do professor deseja alterar: "))
        for professor_dicionario in lista_dados:
            if professor_dicionario["cod_professor"] == codigo:
                alterar_professor = professor_dicionario
                alterar_professor["cod_professor"] = int(input("Informe o novo código: "))
                alterar_professor["nome_professor"] = input("Informe o novo nome do professor: ")
                alterar_professor["cpf_professor"] = input("Informe o novo CPF: ")
                salvar_arquivo(lista_dados, arquivo_professores)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {codigo} do professor na lista")
              
    elif opcao_menu_principal  == 4:
        alterar_turma = None
        codigo = int(input("Qual código da turma deseja alterar: "))
        for turma_dicionario in lista_dados:
            if turma_dicionario["cod_turma"] == codigo:
                alterar_turma = turma_dicionario
                alterar_turma["cod_turma"] = int(input("Informe o novo código da turma: "))
                alterar_turma["cod_professor"] = int(input("Informe o novo código do professor: "))
                alterar_turma["cod_disciplina"] = int(input("Informe novo código da disciplina: "))
                salvar_arquivo(lista_dados, arquivo_turmas)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {codigo} da turma na lista")
        
    else:
        alterar_matricula = None
        codigo = int(input("Qual código da turma deseja alterar: "))
        for matricula_dicionario  in lista_dados:
            if matricula_dicionario["cod_turma"] == codigo:
                alterar_matricula = matricula_dicionario
                alterar_matricula["cod_estudante"] = int(input("Informe o novo código do estudante: "))
                alterar_matricula["cod_turma"] = int(input("Informe o novo código da turma: "))
                salvar_arquivo(lista_dados, arquivo_matriculas)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {codigo} da turma na lista")

    print("Pressione qualquer tecla para continuar")
    msvcrt.getch() # Pausa o sistema até que uma  tecla seja pressionada
    
# Realiza a exclusão do código selecionado
def excluir(opcao_menu_principal, lista_dados):
    print("Opcao do menu operações selecionado: Excluir")
    codigo_nao_encontrado = True
    
    if opcao_menu_principal == 1:
        excluir_codigo = int(input("Qual código do estudante deseja excluir: "))
        
        for estudante_dicionario in lista_dados: # For, vai pesquisar o estudante na lista de estudantes
            if estudante_dicionario["cod_estudante"] == excluir_codigo: # Se o estudante é localizado pelo código solicitado,
                lista_dados.remove(estudante_dicionario)
                salvar_arquivo(lista_dados, arquivo_estudante)
                codigo_nao_encontrado = False
                print(f"Estudante de código {excluir_codigo} excluído com sucesso!")
                
        if codigo_nao_encontrado:  
            print(f"Não foi localizado o código {excluir_codigo} do estudante na lista")
            
    elif opcao_menu_principal == 2:
        excluir_codigo = int(input("Qual código da disciplina deseja excluir: "))
        
        for disciplina_dicionario in lista_dados:
            if disciplina_dicionario["cod_disciplina"] == excluir_codigo:
                lista_dados.remove(disciplina_dicionario)
                salvar_arquivo(lista_dados, arquivo_disciplinas)
                codigo_nao_encontrado  = False
                print(f"Disciplina de código {excluir_codigo} excluído com sucesso!")
        if codigo_nao_encontrado:  
            print(f"Não foi localizado o código {excluir_codigo} da disciplina na lista")                
        
    elif opcao_menu_principal == 3:
        excluir_codigo = int(input("Qual código do professor deseja excluir: "))
         
        for professor_dicionario in lista_dados:
            if professor_dicionario["cod_professor"] == excluir_codigo:
                lista_dados.remove(professor_dicionario)
                salvar_arquivo(lista_dados, arquivo_professores)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {excluir_codigo} do professor na lista")
            
        
    elif opcao_menu_principal == 4:
        excluir_codigo = int(input("Qual código da turma deseja excluir: "))
        
        for turma_dicionario in lista_dados:
            if turma_dicionario["cod_turma"] == excluir_codigo:
                lista_dados.remove(turma_dicionario)
                salvar_arquivo(lista_dados, arquivo_turmas)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {excluir_codigo} da turma na lista")

    else:
        for matricula_dicionario in lista_dados:
            excluir_codigo = int(input("Qual código da turma deseja excluir: "))
            
            if matricula_dicionario["cod_turma"] == excluir_codigo:
                lista_dados.remove(matricula_dicionario)
                salvar_arquivo(lista_dados, arquivo_matriculas)
                codigo_nao_encontrado = False
                
        if codigo_nao_encontrado:
            print(f"Não foi localizado o código {excluir_codigo} da turma na lista")

    print(lista_dados)
        
    print("Pressione qualquer tecla para limpar o terminal e continuar")
    msvcrt.getch() # comando para continuar o programa após preessionar qualquer tecla, como Enter por exemplo


def salvar_arquivo(lista_dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_aberto:
        json.dump(lista_dados, arquivo_aberto, ensure_ascii=False)
        
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo_aberto:
            lista_dados = json.load(arquivo_aberto)
            
        return lista_dados
    except:
        return []

arquivo_estudante = "estudantes.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

lista_dados = []

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
                    dados = ler_arquivo(arquivo_estudante)
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados)    

                # DISCIPLINA
                elif opcao_menu_principal == 2:
                    dados = ler_arquivo(arquivo_disciplinas)
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados)
                
                # PROFESSOR        
                elif opcao_menu_principal == 3:
                    dados = ler_arquivo(arquivo_professores)
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados)
                
                # TURMA        
                elif opcao_menu_principal == 4:
                    dados  = ler_arquivo(arquivo_turmas)
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados)
                
                # MATRICULA        
                elif opcao_menu_principal == 5:
                    dados = ler_arquivo(arquivo_matriculas)
                    executar_operacoes(opcao_menu_principal, opcao_operacao_selecionada, dados)
                        
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