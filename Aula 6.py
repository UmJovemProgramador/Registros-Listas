opcao =0

while opcao!=3:
    print("1 - Cadastrar \n")
    print("2 - Consultar \n")
    print("3 - Sair \n")
    print("4 - Alterar \n")
    print("5 - Remover \n")

    opcao = int(input("Digite a opção \n"))
    if opcao == 1:
        arquivo = open('alunos.txt','a')
        arquivo.write(input("Digite a Matricula:\n"))
        arquivo.write("\n")
        arquivo.write(input("Digite o nome:\n"))
        arquivo.write("\n")
        print("Cadastrado com sucesso \n")
        input("Aperte ENTER para continuar")
    elif opcao ==2:
        arquivo = open('alunos.txt','r')
        cadastro = []
        cadastro = arquivo.readlines()
        num = len(cadastro)
        cont = 0
        while cont < num:
            print("Matricula: ",cadastro[cont]," Nome: ",cadastro[(cont+1)])
            cont = cont + 2
        input("Aperte ENTER para continuar\n")
    elif opcao ==3:
        print("Muito Obrigado, tchau \n")
    elif opcao ==4:
        arquivo = open("alunos.txt", 'r')
        cadastro = []
        cadastro = arquivo.readlines()
        print(cadastro)
        cad = [s.strip() for s in cadastro]
        cont = 0
        num = len(cad)
        busca = False
        mat = input("Digite a matrícula:\n")
        while cont < num:
            if mat == cad[cont]:
                cad[cont] =input("Nova Mat \n")
                cad[cont+1]=input("Novo Nome\n")
                busca = True
                break
            cont = cont + 2
        if busca == False:
            print("Matricula não encontrada \n")
        else:
            arquivo = open("alunos.txt", 'w')
            cont = 0
            num = len(cad)
            while cont < num:
                arquivo.write(cad[cont])
                arquivo.write("\n")
                cont = cont + 1
            input("Digite ENTER para continuar\n")
    elif opcao  ==5:
        arquivo = open("alunos.txt", 'r')
        cadastro = []
        cadastro = arquivo.readlines()
        cad = [s.strip() for s in cadastro]
        busca = False
        cont = 0
        num = len(cad)
        mat = input("Digite a matrícula: \n")
        while cont < num:
            if mat == cad[cont]:
                cad.pop(cont)
                cad.pop(cont)
                busca = True
                break
            cont = cont + 2
        if busca == False:
            print("Matrícula não encontrada")
        else:
            arquivo = open("alunos.txt", 'w')
            cont = 0
            num = len(cad)
            while cont < num:
                arquivo.write(cad[cont])
                arquivo.write("\n")
                cont = cont + 1
                input("Digite ENTER para continuar")
    else:
        print("Opçao Inválida \n")
        input("Aperte ENTER para continuar\n")