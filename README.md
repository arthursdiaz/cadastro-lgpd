# 📋 Sistema de Cadastro de Clientes (Python)

Este é um sistema simples de cadastro de clientes desenvolvido em Python, com foco educacional para o curso de **Análise e Desenvolvimento de Sistemas - PIM II (1º semestre)**. Ele integra conceitos de **Programação**, **Redes**, **Segurança da Informação** e **LGPD**.

---

## ⚙️ Funcionalidades

- Cadastro de clientes com:
  - Nome
  - E-mail
  - Telefone
  - CPF (com criptografia de segurança)
- Validação de CPF e e-mail
- Salvamento dos dados em arquivo `clientes.json`
- Visualização da lista de clientes cadastrados
- Exibição de informações do sistema:
  - Nome do computador (hostname)
  - IP local
  - Arquivo de dados
  - Protocolo TCP/IP

---

## 🔐 Segurança e LGPD

O CPF do cliente é armazenado no formato **criptografado com hash MD5**, para garantir a segurança dos dados e estar em conformidade com a **LGPD (Lei Geral de Proteção de Dados)**.  
> ⚠️ *Obs: MD5 é usado aqui apenas com fins educativos. Para sistemas reais, recomenda-se utilizar algoritmos mais seguros como SHA-256 ou criptografia simétrica com chave.*

---

## 📂 Estrutura dos Arquivos

- `clientes.json`: arquivo onde os dados dos clientes são armazenados.
- `main.py`: script principal com o sistema de cadastro.

---

## ▶️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
