
import time # pausa por  alguns segundos
from datetime import datetime, timedelta #manopulação de datas e horas
import importlib# para importar módulos 
plt = None 
try:# usamos o try para tentar carregar o módulo
 
    matplotlib = importlib.import_module('matplotlib')# tenta importar o matplotlib
    plt = importlib.import_module('matplotlib.pyplot')# tenta importar o pyplot
except Exception:# caso o modulo não esteja instalado, captura o erro
    print("Atenção: A biblioteca 'matplotlib' não está instalada.")# avisa o usuário
    print("Para usar a função de gráfico, instale-a com: pip install matplotlib")# instrução para instalar
    plt = None# define plt como None para evitar erros posteriores

# ---  DEFINIÇÃO DAS ESTRUTURAS DE DADOS ---
biblioteca = []# lista que armazena os livros 

emprestimos = []# lista que armazena os empréstimos

pedidos = []# lista que armazena os pedidos de livros

# ---  DEFINIÇÃO DAS FUNÇÕES  ---

# ---  CADASTRAR UM LIVRO ---
def cadastrar_livro():# cadastra um novo livro na biblioteca.
        
    print("\n--- Cadastro de Novo Livro ---")# cabeçalho da seção de cadastro
    titulo = input("Digite o título do livro: ").strip()# pede o título do livro e remove espaços extras
    autor = input("Digite o autor do livro: ").strip()# pede o autor do livro e remove espaços extras
    genero = input("Digite o gênero do livro: ").strip()# pede o gênero do livro e remove espaços extras
    
    while True: # Loop infinito que só para quando a entrada for válida.
        try:#' tenta converter a entrada para inteiro
            
            quantidade = int(input("Digite a quantidade disponível: "))# pede a quantidade disponível e converte para inteiro
            break # se a conversão for bem-sucedida, sai do loop
        except ValueError:# se a conversão falhar, captura o erro
           
            print("Entrada inválida. Por favor, digite um número inteiro.")# avisa o usuário sobre a entrada inválida

    novo_livro = { 'titulo': titulo, 'autor': autor, 'genero': genero, 'quantidade': quantidade }# cria um dicionário com os dados do novo livro
    
    biblioteca.append(novo_livro)# adiciona o novo livro à lista da biblioteca
    print(f"\nO livro '{titulo}' foi cadastrado com sucesso!")# confirma o cadastro do livro
   
    pedidos_atendidos = []# lista para armazenar pedidos que serão atendidos
    for pedido in pedidos: # percorre a lista de pedidos
        # 
        if pedido['titulo'].lower() == titulo.lower():# compara o título do pedido com o título do livro cadastrado, ignorando maiúsculas/minúsculas
           
            print(f"--- NOTIFICAÇÃO ENVIADA ---")# cabeçalho da notificação
            print(f"Para: {pedido['email']}")# mostra o e-mail do destinatário
            print(f"Assunto: O livro '{pedido['titulo']}' já está disponível!")# assunto do e-mail
           
            pedidos_atendidos.append(pedido)# adiciona o pedido à lista de pedidos atendidos
    
    if pedidos_atendidos:# se houver pedidos atendidos
       
        globals()['pedidos'] = [p for p in pedidos if p not in pedidos_atendidos]# atualiza a lista global de pedidos removendo os atendidos
        print("\nLista de pedidos foi atualizada.")# confirma a atualização da lista de pedidos


# ---  LISTAR TODOS OS LIVROS ---
def listar_livros():# lista todos os livros cadastrados na biblioteca.
 
    if not biblioteca:# verifica se a lista de livros está vazia
        print("\nNenhum livro cadastrado na biblioteca ainda.")# avisa que não há livros cadastrados
        return # 'return' para a execução da função aqui.
   
    print("\n--- Lista de Livros na Biblioteca ---")# cabeçalho da seção de listagem de livros
    for livro in biblioteca: # percorre cada livro na lista da biblioteca
        
        print(f"'{livro['titulo']}' por {livro['autor']} | Gênero: {livro['genero']}, Quantidade: {livro['quantidade']}")# mostra os detalhes do livro


# --- BUSCAR E OFERECER RETIRADA DE UM LIVRO ---
def buscar_livro():# busca um livro pelo título e oferece a opção de retirá-lo.
  
    titulo_busca = input("\nDigite o título do livro que deseja buscar: ").strip()# pede o título do livro a ser buscado e remove espaços extras
    livro_encontrado = None # variável para armazenar o livro encontrado, se houver

    for livro in biblioteca:# percorre cada livro na lista da biblioteca
        if livro['titulo'].lower() == titulo_busca.lower():# compara o título do livro com o título buscado, ignorando maiúsculas/minúsculas
            livro_encontrado = livro# se encontrar, armazena o livro na variável
            break # sai do loop após encontrar o livro
    
    if livro_encontrado: # se o livro foi encontrado...
        
        print("\n--- Livro Encontrado ---")# cabeçalho da seção de livro encontrado
        print(f"Título: {livro_encontrado['titulo']}")# mostra o título do livro
        print(f"Autor: {livro_encontrado['autor']}")# mostra o autor do livro
        print(f"Gênero: {livro_encontrado['genero']}")# mostra o gênero do livro
        print(f"Quantidade Disponível: {livro_encontrado['quantidade']}")# mostra a quantidade disponível do livro

        deseja_retirar = input("\nDeseja retirar este livro? (S/N): ").strip().lower()# pergunta se o usuário deseja retirar o livro
        if deseja_retirar == 's':# se a resposta for sim...

            if livro_encontrado['quantidade'] > 0:# verifica se há cópias disponíveis para retirada
                nome_estudante = input("Digite o nome completo do estudante: ").strip()# pede o nome do estudante e remove espaços extras
                ra_estudante = input(f"Digite o RA de {nome_estudante}: ").strip()# pede o RA do estudante e remove espaços extras
                livro_encontrado['quantidade'] -= 1# atualiza a quantidade disponível do livro
                data_devolucao = (datetime.now() + timedelta(days=90)).strftime('%d/%m/%Y')# calcula a data de devolução (90 dias a partir de hoje) e formata como string
                novo_emprestimo = { 'titulo': livro_encontrado['titulo'], 'estudante': nome_estudante, 'ra': ra_estudante, 'data_devolucao': data_devolucao }# cria um dicionário com os dados do novo empréstimo
                emprestimos.append(novo_emprestimo)# adiciona o novo empréstimo à lista de empréstimos
                print("\n--- Retirada Realizada com Sucesso ---")
                print(f"Livro: {livro_encontrado['titulo']}, Devolução até: {data_devolucao}")# confirma a retirada do livro e informa a data de devolução
            else:
                print(f"\nDesculpe, não há cópias de '{livro_encontrado['titulo']}' disponíveis.")# avisa que não há cópias disponíveis
    else: 
        print(f"\nO livro '{titulo_busca}' não foi encontrado.")# avisa que o livro não foi encontrado
        deseja_pedir = input("Deseja fazer um pedido para este livro? (S/N): ").strip().lower()# pergunta se o usuário deseja fazer um pedido para o livro
        if deseja_pedir == 's':# se a resposta for sim...
            email_usuario = input("Por favor, digite seu e-mail para ser notificado: ").strip()# pede o e-mail do usuário e remove espaços extras
            pedidos.append({'titulo': titulo_busca, 'email': email_usuario})# adiciona o pedido à lista de pedidos
            print(f"\nPedido realizado com sucesso! Você será notificado em '{email_usuario}'.")# confirma o pedido





# --- DEVOLVER LIVRO ---
def devolver_livro():
    """Permite devolver um livro emprestado, atualiza quantidade e remove o empréstimo."""
    if not emprestimos:
        print("\nNão há empréstimos registrados no momento.")
        return

    titulo = input("\nDigite o título do livro que deseja devolver: ").strip()
    ra = input("Digite o RA do estudante que pegou o livro: ").strip()

    emprestimo_encontrado = None
    for e in emprestimos:
        if e['titulo'].lower() == titulo.lower() and e.get('ra', '').strip() == ra:
            emprestimo_encontrado = e
            break

    if emprestimo_encontrado:
        # atualiza a quantidade do livro na biblioteca, se existir
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower():
                livro['quantidade'] += 1
                break

        emprestimos.remove(emprestimo_encontrado)
        print(f"\nDevolução realizada com sucesso: '{titulo}' por RA {ra}.")
    else:
        print(f"\nEmpréstimo não encontrado para o livro '{titulo}' e RA {ra}.")

# --- AÇÃO: LISTAR OS PEDIDOS PENDENTES ---
def listar_pedidos():
    """Mostra todos os livros que foram solicitados pelos usuários."""
    print("\n--- Lista de Pedidos de Livros Pendentes ---")
    if not pedidos:
        print("Nenhum pedido pendente no momento.")
    else:
        for i, pedido in enumerate(pedidos, 1):
            print(f"{i}. Título: {pedido['titulo']} | Pedido por: {pedido['email']}")


# ---  GERAR UM GRÁFICO DE GÊNEROS ---
def gerar_grafico_generos():# gera um gráfico de barras mostrando a quantidade de livros por gênero.
    
    if plt is None:# verifica se a biblioteca matplotlib foi carregada com sucesso
        print("\nOperação cancelada. A biblioteca 'matplotlib' é necessária para gerar gráficos.")
        return
    if not biblioteca:# verifica se há livros cadastrados na biblioteca
        print("\nNão há livros cadastrados para gerar um gráfico.")# avisa que não há livros cadastrados
        return

    contagem_generos = {}# dicionário para armazenar a contagem de livros por gênero
    for livro in biblioteca:# percorre cada livro na lista da biblioteca
        genero = livro['genero']# obtém o gênero do livro
        quantidade = livro['quantidade']# obtém a quantidade disponível do livro
        if genero in contagem_generos:# se o gênero já está no dicionário, soma a quantidade
            contagem_generos[genero] += quantidade# soma a quantidade existente
        else:
            contagem_generos[genero] = quantidade# inicializa a contagem para este gênero
    
    generos = list(contagem_generos.keys())      # Lista de nomes dos gêneros
    quantidades = list(contagem_generos.values()) # Lista de totais de cada gênero
    
    fig, ax = plt.subplots()# cria uma figura e um conjunto de eixos
    ax.bar(generos, quantidades, color='skyblue') # Cria as barras
    ax.set_ylabel('Quantidade de Livros')         # Rótulo do eixo Y
    ax.set_xlabel('Gêneros')                      # Rótulo do eixo X
    ax.set_title('Quantidade de Livros por Gênero na Biblioteca') # Título do gráfico
    
    plt.show()# exibe o gráfico
    print("\nGráfico gerado com sucesso!")


# ---  O MENU PRINCIPAL  ---
def menu():#
    
    if not biblioteca:#  adiciona alguns livros  para demonstração
        biblioteca.append({'titulo': 'Harry Potter', 'autor': 'J.K. Rowling', 'genero': 'Fantasia', 'quantidade': 1})
        biblioteca.append({'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia', 'quantidade': 4})
        biblioteca.append({'titulo': 'Neuromancer', 'autor': 'William Gibson', 'genero': 'Ficção Científica', 'quantidade': 2})
        biblioteca.append({'titulo': 'Dracula', 'autor': 'Bram Stoker', 'genero': 'Terror', 'quantidade': 6}) 
        biblioteca.append({'titulo': 'It - A Coisa', 'autor': 'Stephen King', 'genero': 'Terror', 'quantidade': 5})  
        biblioteca.append({'titulo': '1984', 'autor': 'George Orwell', 'genero': 'Distopia', 'quantidade': 3})
        biblioteca.append({'titulo': 'Admirável Mundo Novo', 'autor': 'Aldous Huxley', 'genero': 'Distopia', 'quantidade': 2})
    
    while True:# loop infinito para o menu principal

        # Mostramos as opções disponíveis.
        print("\n--- Bem-vindo à Biblioteca Anhanguera ---")
        print("1. Listar todos os livros")
        print("2. Cadastrar novo livro")
        print("3. Buscar e Retirar livro")
        print("4. Devolver livro")
        print("5. Ver lista de pedidos")
        print("6. Gerar Gráfico de Gêneros")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ").strip()# pede a opção do usuário e remove espaços extras
       # Com base na opção, chamamos a função correspondente.
        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            cadastrar_livro()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            devolver_livro()
        elif opcao == '5':
            listar_pedidos()
        elif opcao == '6':
            gerar_grafico_generos()
        elif opcao == '7':
            print("\nObrigado por utilizar nossa biblioteca...")
            time.sleep(1)
            break # 'break' é o único comando que pode quebrar este loop e encerrar o programa.
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
        time.sleep(2)# pausa por 2 segundos antes de mostrar o menu novamente
        
            

      


if __name__ == "__main__":# primeira coisa que o Python faz ao rodar este arquivo
    menu()# chamar a função do menu principal