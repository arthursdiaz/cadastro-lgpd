
import json
import os
import hashlib

def criptografar_cpf(cpf):
    # Criptografia simples pro CPF (LGPD)
    # Usando hash MD5 - conceito de segurança
    return hashlib.md5(cpf.encode()).hexdigest()

def validar_cpf(cpf):
    # Remove pontos e traços
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    # Verifica se tem 11 números
    if len(cpf_limpo) != 11:
        return False
    
    # Verifica se é só números
    if not cpf_limpo.isdigit():
        return False
        
    return True

def validar_email(email):
    # Validação bem básica
    if "@" in email and "." in email:
        return True
    return False

def cadastrar():
    print("\n=== CADASTRO DE CLIENTE ===")
    
    # Pede os dados
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    cpf = input("Digite o CPF: ")
    
    # Validações
    if len(nome) < 2:
        print("Nome muito pequeno!")
        return
        
    if not validar_email(email):
        print("Email inválido!")
        return
        
    if not validar_cpf(cpf):
        print("CPF inválido!")
        return
    
    # Monta o dicionário do cliente
    cliente = {
        "nome": nome,
        "email": email,  
        "telefone": telefone,
        "cpf_hash": criptografar_cpf(cpf)  # Criptografado por causa da LGPD
    }
    
    # Carrega a lista atual ou cria uma nova
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r") as arquivo:
            lista_clientes = json.load(arquivo)
    else:
        lista_clientes = []
    
    # Adiciona o novo cliente
    lista_clientes.append(cliente)
    
    # Salva no arquivo
    with open("clientes.json", "w") as arquivo:
        json.dump(lista_clientes, arquivo, indent=4)
    
    print("Cliente cadastrado com sucesso!")

def listar():
    print("\n=== LISTA DE CLIENTES ===")
    
    if not os.path.exists("clientes.json"):
        print("Nenhum cliente cadastrado ainda.")
        return
    
    with open("clientes.json", "r") as arquivo:
        lista_clientes = json.load(arquivo)
    
    if len(lista_clientes) == 0:
        print("Lista vazia.")
        return
    
    for i, cliente in enumerate(lista_clientes):
        print(f"\nCliente {i+1}:")
        print(f"Nome: {cliente['nome']}")
        print(f"Email: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"CPF: *** (criptografado)")

def info_sistema():
    # Mostra informações de rede - disciplina Redes
    import socket
    
    print("\n=== INFORMAÇÕES DO SISTEMA ===")
    try:
        nome_pc = socket.gethostname()
        ip_local = socket.gethostbyname(nome_pc)
        print(f"Nome do PC: {nome_pc}")
        print(f"IP Local: {ip_local}")
    except:
        print("Erro ao obter informações de rede")
    
    print("Arquivo de dados: clientes.json")
    print("Protocolo usado: TCP/IP")

def menu():
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE CADASTRO")
        print("="*30)
        print("1 - Cadastrar cliente")
        print("2 - Ver clientes")
        print("3 - Info do sistema") 
        print("0 - Sair")
        
        opcao = input("\nDigite sua opção: ")
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            info_sistema()
        elif opcao == "0":
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Roda o programa
if __name__ == "__main__":
    menu()