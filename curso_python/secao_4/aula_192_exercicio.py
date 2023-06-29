# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista_comandos = ["listar", "desfazer", "refazer"]
lista_tarefas = []
lista_backup =[]
while True:
    print("Comandos: listar, desfazer, refazer")
    comando = input("Digite uma tarefa ou comando: ").lower().strip()
    
    if comando in lista_comandos:
        if comando == "listar" or comando == "desfazer":
            if len(lista_tarefas) == 0:
                print("Não há tarefas adicionadas ainda")
            elif comando == "listar":
                for tarefa in lista_tarefas:
                    print(f"\t{tarefa}")
            elif comando == "desfazer":
                lista_backup.append(lista_tarefas.pop())
        elif comando == "refazer":
            if len(lista_backup) == 0:
                print("Não há tarefas para recuperar")
            else:
                lista_tarefas.append(lista_backup.pop())
    else:
        lista_tarefas.append(comando)
        