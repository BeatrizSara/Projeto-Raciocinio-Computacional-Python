# Menu principal 
print("==== Menu de Opções ==== ")
print("1. Estudante")
print("2. Disciplina")
print("3. Professor")
print("4. Turma")
print("5. Matricula")
print("0. Sair do Sistema")
# Coleta da opção 1 escolida pelo usuário
opcao = int(input("Informe uma opção válida: "))
print("===============================")

# Verificação da opcao informada pelo usuário
if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
    
    if opcao == 1:
        print("Opção Estudante")
        print("Menu de Operações - Opção {}".format(opcao))
        print("1. Incluir")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")
        # Coleta da opção secundaria do usuario
        opcao_2 = int(input("Informe uma opção válida: "))
        print("Escolheu a opção {}".format(opcao_2))
        print("===============================")
    elif opcao == 2:
        print("Opção Disciplina")
        print("Menu de Operações - Opção {}".format(opcao))
        print("1. Incluir")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")
        # Coleta da opção secundaria do usuario
        opcao_2 = int(input("Informe uma opção válida: "))
        print("Escolheu a opção {}".format(opcao_2))
        print("===============================")
    elif opcao == 3:
        print("Opção Professor")
        print("Menu de Operações - Opção {}".format(opcao))
        print("1. Incluir")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")
        # Coleta da opção secundaria do usuario
        opcao_2 = int(input("Informe uma opção válida: "))
        print("Escolheu a opção {}".format(opcao_2))
        print("===============================")    
    elif opcao == 4:
        print("Opção Turma")
        print("Menu de Operações - Opção {}".format(opcao))
        print("1. Incluir")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")
        # Coleta da opção secundaria do usuario
        opcao_2 = int(input("Informe uma opção válida: "))
        print("Escolheu a opção {}".format(opcao_2))
        print("===============================")  
    elif opcao == 5:
        print("Opção Matrícula")
        print("Menu de Operações - Opção {}".format(opcao))
        print("1. Incluir")
        print("2. Listar")
        print("3. Alterar")
        print("4. Excluir")
        print("5. Voltar ao menu anterior")
        # Coleta da opção secundaria do usuario
        opcao_2 = int(input("Informe uma opção válida: "))
        print("Escolheu a opção {}".format(opcao_2))
        print("===============================")
# Verificação da opção "sair do sistema"
elif opcao == 0:
    print("Opção selecionada: Sair do sistema")
# Informar opção Inválida ao usuário
else:
    print("Opção INVÁLIDA")
    print("Tente novamente")