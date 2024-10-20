import sqlite3
import datetime
import os

class Cliente:
    def __init__(self, id, nome, endereco, telefone, celular, data_cadastro):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.celular = celular
        self.data_cadastro = data_cadastro

class OrdemDeServico:
    def __init__(self, id, cliente_id, data_inicio, data_termino):
        self.id = id
        self.cliente_id = cliente_id
        self.data_inicio = data_inicio
        self.data_termino = data_termino

class Checklist:
    def __init__(self, id, cliente_id, itens):
        self.id = id
        self.cliente_id = cliente_id
        self.itens = itens

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('controle_acesso.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        telefone TEXT,
        celular TEXT,
        data_cadastro TEXT)
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrdensDeServico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        data_inicio TEXT,
        data_termino TEXT,
        FOREIGN KEY(cliente_id) REFERENCES Clientes(id))
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Checklists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        itens TEXT,
        FOREIGN KEY(cliente_id) REFERENCES Clientes(id))
''')

# Adicionar usuário e senha para autenticação
usuarios = {"leandro": "leo380l"}

def autenticar():
    while True:
        input_usuario = input("Usuário: ")
        input_senha = input("Senha: ")
        if input_usuario in usuarios and usuarios[input_usuario] == input_senha:
            print("Autenticação bem-sucedida!")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
import sqlite3
import datetime
import os

class Cliente:
    def __init__(self, id, nome, endereco, telefone, celular, data_cadastro):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.celular = celular
        self.data_cadastro = data_cadastro

class OrdemDeServico:
    def __init__(self, id, cliente_id, data_inicio, data_termino):
        self.id = id
        self.cliente_id = cliente_id
        self.data_inicio = data_inicio
        self.data_termino = data_termino

class Checklist:
    def __init__(self, id, cliente_id, itens):
        self.id = id
        self.cliente_id = cliente_id
        self.itens = itens

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('controle_acesso.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        telefone TEXT,
        celular TEXT,
        data_cadastro TEXT)
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrdensDeServico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        data_inicio TEXT,
        data_termino TEXT,
        FOREIGN KEY(cliente_id) REFERENCES Clientes(id))
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Checklists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        itens TEXT,
        FOREIGN KEY(cliente_id) REFERENCES Clientes(id))
''')

# Adicionar usuário e senha para autenticação
usuarios = {"leandro": "leo380"}

def autenticar():
    while True:
        input_usuario = input("Usuário: ")
        input_senha = input("Senha: ")
        if input_usuario in usuarios and usuarios[input_usuario] == input_senha:
            print("Autenticação bem-sucedida!")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

# Adicionar usuário e senha para autenticação
usuario = "leandro"
senha = "leo380"

def autenticar():
    while True:
        input_usuario = input("Usuário: ")
        input_senha = input("Senha: ")
        if input_usuario == usuario and input_senha == senha:
            print("Autenticação bem-sucedida!")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

clientes = []
ordens_de_servico = []
checklists = []

def adicionar_cliente():
    nome = input("Nome do cliente: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    celular = input("Celular: ")
    data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
    INSERT INTO Clientes (nome, endereco, telefone, celular, data_cadastro)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, endereco, telefone, celular, data_cadastro))
    conn.commit()
    print("Cliente adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def listar_clientes():
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Endereço: {cliente[2]}, Telefone: {cliente[3]}, Celular: {cliente[4]}, Data de Cadastro: {cliente[5]}")
    input("Pressione Enter para continuar...")

def adicionar_ordem_de_servico():
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    data_inicio = input("Data de início (YYYY-MM-DD): ")
    data_termino = input("Data de término (YYYY-MM-DD): ")
    cursor.execute('''
    INSERT INTO OrdensDeServico (cliente_id, data_inicio, data_termino)
    VALUES (?, ?, ?)
    ''', (cliente_id, data_inicio, data_termino))
    conn.commit()
    print("Ordem de serviço adicionada com sucesso!")
    input("Pressione Enter para continuar...")

def listar_ordens_de_servico():
    cursor.execute('SELECT * FROM OrdensDeServico')
    ordens = cursor.fetchall()
    for ordem in ordens:
        print(f"ID: {ordem[0]}, Cliente ID: {ordem[1]}, Data de Início: {ordem[2]}, Data de Término: {ordem[3]}")
        print("--------------------------------------------------")
    input("Pressione Enter para continuar...")

def adicionar_checklist():
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    itens = input("Itens do checklist (separados por vírgula): ").split(',')
    cursor.execute('''
    INSERT INTO Checklists (cliente_id, itens)
    VALUES (?, ?)
    ''', (cliente_id, ', '.join(itens)))
    conn.commit()
    print("Checklist adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def listar_checklists():
    cursor.execute('SELECT * FROM Checklists')
    checklists = cursor.fetchall()
    for checklist in checklists:
        print(f"ID: {checklist[0]}, Cliente ID: {checklist[1]}, Itens: {checklist[2]}")
        print("--------------------------------------------------")
    input("Pressione Enter para continuar...")

def agendar_suporte_tecnico():
    listar_clientes()
    cliente_id = int(input("ID do cliente: "))
    data_inicio = input("Data de agendamento (YYYY-MM-DD): ")
    cursor.execute('''
    INSERT INTO OrdensDeServico (cliente_id, data_inicio, data_termino)
    VALUES (?, ?, ?)
    ''', (cliente_id, data_inicio, "Agendamento de Suporte Técnico Presencial"))
    conn.commit()
    print("Suporte técnico agendado com sucesso!")
    input("Pressione Enter para continuar...")

def imprimir_dados(tabela):
    cursor.execute(f'SELECT * FROM {tabela}')
    dados = cursor.fetchall()
    for dado in dados:
        print(dado)
    input("Pressione Enter para continuar...")

def imprimir_etiqueta():
    listar_ordens_de_servico()
    ordem_id = int(input("ID da ordem de serviço: "))
    cursor.execute('SELECT * FROM OrdensDeServico WHERE id = ?', (ordem_id,))
    ordem = cursor.fetchone()
    if ordem:
        cursor.execute('SELECT * FROM Clientes WHERE id = ?', (ordem[1],))
        cliente = cursor.fetchone()
        print("--------------------------------------------------")
        print(f"Ordem de Serviço: {ordem[0]}")
        print(f"Cliente: {cliente[1]}")
        print(f"Telefone: {cliente[3]}")
        print("--------------------------------------------------")
    else:
        print("Ordem de serviço não encontrada!")
    input("Pressione Enter para continuar...")

def pesquisar_dados():
    termo = input("Digite o termo de pesquisa: ")
    cursor.execute('''
    SELECT * FROM Clientes WHERE nome LIKE ? OR endereco LIKE ? OR telefone LIKE ? OR celular LIKE ?
    ''', (f'%{termo}%', f'%{termo}%', f'%{termo}%', f'%{termo}%'))
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)
    input("Pressione Enter para continuar...")

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------------------------------------------------")
        print("**SHAYRA INFORMATICA**")
        print("Telefone: 11-994780422 (WhatsApp)")
        print("Email: shayra.forfor.guarulhos@gmail.com")
        print("--------------------------------------------------")
        print("\nMenu:")
        print("1. Adicionar Cliente")
        print("2. Adicionar Ordem de Serviço")
        print("3. Listar Clientes")
        print("4. Listar Ordens de Serviço")
        print("5. Agendar Suporte Técnico Presencial")
        print("6. Adicionar Checklist")
        print("7. Listar Checklists")
        print("8. Imprimir Clientes")
        print("9. Imprimir Ordens de Serviço")
        print("10. Imprimir Checklists")
        print("11. Imprimir Etiqueta")
        print("12. Pesquisar Dados")
        print("13. Sair")
        print("--------------------------------------------------")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_cliente()
        elif opcao == 2:
            adicionar_ordem_de_servico()
        elif opcao == 3:
            listar_clientes()
        elif opcao == 4:
            listar_ordens_de_servico()
        elif opcao == 5:
            agendar_suporte_tecnico()
        elif opcao == 6:
            adicionar_checklist()
        elif opcao == 7:
            listar_checklists()
        elif opcao == 8:
            imprimir_dados('Clientes')
        elif opcao == 9:
            imprimir_dados('OrdensDeServico')
        elif opcao == 10:
            imprimir_dados('Checklists')
        elif opcao == 11:
            imprimir_etiqueta()
        elif opcao == 12:
            pesquisar_dados()
        elif opcao == 13:
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    autenticar()
    menu()
    conn.close()