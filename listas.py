
# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa à lista
def adicionarTarefa(tarefa):
    tarefas.append({'nome': tarefa, 'concluida': False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para remover uma tarefa da lista
def removerTarefa(tarefa):
    for t in tarefas:
        if t['nome'] == tarefa:
            tarefas.remove(t)
            print(f"Tarefa '{tarefa}' removida com sucesso!")
            return
    print(f"Tarefa '{tarefa}' não encontrada!")

# Função para marcar uma tarefa como concluída
def concluirTarefa(tarefa):
    for t in tarefas:
        if t['nome'] == tarefa:
            t['concluida'] = True
            print(f"Tarefa '{tarefa}' marcada como concluída!")
            return
    print(f"Tarefa '{tarefa}' não encontrada!")

# Função para exibir todas as tarefas na lista
def listarTarefas():
    if not tarefas:
        print("Não há tarefas na lista.")
        return
    print("Lista de Tarefas:")
    for t in tarefas:
        status = "Concluída" if t['concluida'] else "Não concluída"
        print(f"- {t['nome']} ({status})")

# Função para listar tarefas com base em seu status de conclusão
def listarTarefasPorStatus(concluidas=True):
    if not tarefas:
        print("Não há tarefas na lista.")
        return
    status_str = "concluídas" if concluidas else "não concluídas"
    print(f"Lista de Tarefas {status_str}:")
    for t in tarefas:
        if t['concluida'] == concluidas:
            print(f"- {t['nome']}")

# Menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Concluir Tarefa")
        print("4. Listar Todas as Tarefas")
        print("5. Listar Tarefas Concluídas")
        print("6. Listar Tarefas Não Concluídas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            tarefa = input("Digite a descrição da tarefa: ")
            adicionarTarefa(tarefa)
        elif opcao == '2':
            tarefa = input("Digite a descrição da tarefa a ser removida: ")
            removerTarefa(tarefa)
        elif opcao == '3':
            tarefa = input("Digite a descrição da tarefa a ser concluída: ")
            concluirTarefa(tarefa)
        elif opcao == '4':
            listarTarefas()
        elif opcao == '5':
            listarTarefasPorStatus(concluidas=True)
        elif opcao == '6':
            listarTarefasPorStatus(concluidas=False)
        elif opcao == '7':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executar o menu
if __name__ == "__main__":
    menu()
