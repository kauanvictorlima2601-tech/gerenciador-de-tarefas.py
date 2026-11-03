concluidas = []
pendentes = []
while True:
    print(" ")
    print("---Gerenciador de Tarefas---")
    print("1. Adicionar Tarefa ")
    print("2. Listar Tarefas ")
    print("3. Concluir Tarefa ")
    print("4. Remover Tarefa ")
    print("5. Sair ")
    print(" ")
    opção = input("Escolha uma opção: ")
    print(" ")

    #adicionar tarefas
    if opção == "1": 
        tarefa = input("Qual tarefa deseja adicionar? ")
        print("Adicionando tarefa...")
        pendentes.append(tarefa)
        print(f"Tarefa {tarefa} adicionada!")
        

    #listar tarefas
    elif opção == "2":
        print("Listando tarefas...")
        print("---Tarefas Pendentes---")
        for i in range(len(pendentes)):
            print(f"{1+i}. {pendentes[i]}")
        if pendentes == []:
            print("Não há nenhuma tarefa cadastrada")
        print(" ")
        print("---Tarefas Concluídas---")
        for ii in range(len(concluidas)):
            print(f"{1+ii}. {concluidas[ii]}")
        if concluidas == []:
            print("Não há nenhuma tarefa concluída")


    #concluir tarefa
    elif opção == "3":
        print("---Tarefas Pendentes---")
        for n in range(len(pendentes)):
            print(f"{1+n}. {pendentes[n]}")
        print(" ")
        if not pendentes:
            print("Não restam tarefas pendentes")
        if pendentes:
            try: 
                escolha = int(input("Qual tarefa você deseja concluir ou já concluiu? "))
                if escolha > len(pendentes) or escolha < 1:
                    print("Número inválido")
                else:
                    n = escolha - 1
                    tarefa = pendentes[n]
                    print("Concluindo tarefa...")
                    print(f"Tarefa {tarefa} concluída!")
                    pendentes.pop(n)
                    concluidas.append(tarefa)
            except ValueError:
                print("Expressão inválida: digite um número inteiro")


    #remover tarefa
    elif opção == "4":
        try:
            tipo_tarefa = int(input("Qual tipo de tarefa você deseja remover? Digite 1 para concluída e 2 para pendentes: "))
            if tipo_tarefa < 1 or tipo_tarefa > 2:
                print(f"Só números de 1 a 2")
            else:
                if tipo_tarefa == 2:
                    for j in range(len(pendentes)):
                        print("---Tarefas Pendentes---")
                        print(f"{1+j}. {pendentes[j]}")
                    if not pendentes:
                        print("Não restam tarefas pendentes")
                    else:
                        try: 
                            remoção = int(input("Qual tarefa pendente você deseja remover? "))
                            if remoção > len(pendentes) or remoção < 1:
                                print("Número inválido: tente novamente")
                            else: 
                                j = remoção - 1
                                tarefa = pendentes[j]
                                print("Removendo tarefa...")
                                pendentes.pop(j)
                                print(f"Tarefa {tarefa} removida!")
                        except ValueError:
                            print("Expressão inválida: digite um número inteiro")
                elif tipo_tarefa == 1:
                    print("---Tarefas Concluídas---")
                    for _ in range(len(concluidas)):
                        print(f"{1+_}. {concluidas[_]}")
                    if not concluidas:
                        print("Não restam tarefas concluídas")
                    else: 
                        try: 
                            remoçãoII = int(input("Qual tarefa concluída você deseja remover? "))
                            if remoçãoII > len(concluidas) or remoçãoII < 1:
                                print("Número inválido: tente novamente")
                            else:
                                _ = remoçãoII - 1
                                tarefa = concluidas[_]
                                print("Removendo tarefa...")
                                concluidas.pop(_)
                                print(f"Tarefa {tarefa} removida!")
                        except ValueError:
                            print("Expressão inválida: digite um número inteiro")
        except ValueError:
            print("Expressão inválida: digite um número inteiro")


    #sair
    elif opção == "5":
        print("Saindo do Gerenciador de Tarefas...")
        break

    else:
        print("Opção inválida!")