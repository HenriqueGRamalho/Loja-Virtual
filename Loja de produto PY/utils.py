from getpass import getpass
import os

def valida_usuario():
    logado = False
    while True: 
        arquivo = open("arquivos/usuarios.txt", 'r')
        user_atual = input("Digite o usuario: ")
        senha_atual = getpass("Digite a senha: ")

        for i in arquivo:
          user_arquivo = i.split(";")[0] 
          senha_arquivo = i.split(";")[1].replace("\n", "")

          if user_atual == user_arquivo and senha_atual == senha_arquivo:
            logado = True
            print("Logado com Sucesso!")

        if logado:
          return user_atual
        else:
          print("Usuário ou Senha Incorretas")
          return False

def cadastra_usuario():
  qtde_user = int(input("Quantos usuários gostaria de cadastrar? "))
  users = []
  passw = []

  for _ in range(qtde_user):
    users.append(input("\nQual o login do usuário: "))
    passw.append(getpass("Digite a senha do usuário: "))

  if not os.path.exists("arquivos/"):
      os.makedirs("arquivos")

  with open("arquivos/usuarios.txt", "a+") as arq_users:
    for indice, user in enumerate(users):
      arq_users.write(user + ";" + passw[indice])
      arq_users.write("\n")


def cadastra_produtos():
  qtde_prods = int(input("Quantos produtos gostaria de cadastrar? "))
  produtos = []
  precos = []

  for _ in range(qtde_prods):
    produtos.append(input("\nQual o nome do produto: "))
    precos.append(float(input("Digite o preço do produto: ")))

  with open("arquivos/produtos.txt", "a+") as arq_prods:
    for indice, produto in enumerate(produtos):
      arq_prods.write(produto + ";" + str(precos[indice]))
      arq_prods.write("\n")

def cadastra_admin():
    qtde_admin = int(input("Digite a quantidade de administradores que deseja cadastrar: "))
    admin = []
    senha_admin = []
    for _ in range(qtde_admin): 
        admin.append(input("\nQual o usuário do administrador? "))
        senha_admin.append(input("Digite a senha do administrador: "))
        with open("arquivos/cadastroadmin.txt", "a+") as cadastro_admin:
            for senha, adm in enumerate(admin):
                cadastro_admin.write(adm + ";" + senha_admin[senha])
                cadastro_admin.write("\n")

def valida_admin():
    logado = False
    while True: 
        arquivo = open("arquivos/cadastroadmin.txt", 'r')
        user_atual = input("Digite o usuario do Administrador: ")
        senha_atual = getpass("Digite a senha: ")

        for i in arquivo:
          user_arquivo = i.split(";")[0] 
          senha_arquivo = i.split(";")[1].replace("\n", "")

          if user_atual == user_arquivo and senha_atual == senha_arquivo:
            logado = True
            print("Logado com Sucesso!")

        if logado:
          return user_atual
        else:
          print("Usuário ou Senha Incorretas")
          return False

def cartao_credito():
   titular = input("Digite o nome do Titular: ")
   numero = (input("Digite o número do cartão"))
   validade = input("Digite a validade do cartão: ")
   cvv = (input("Digite o código de segurança do cartão: "))
   if len(numero) == 16 and len(cvv) == 3:
      print("Cartão cadastrado com sucesso!!!\n")
   else:
      print("Credenciais incorretas!!!") 
      exit()