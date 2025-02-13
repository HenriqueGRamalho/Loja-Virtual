import utils

print("Por favor, faça seu login para acessar nossa loja")
admin = input("Você é um administrador? Digite 'sim' ou 'não ")

if admin.lower() == "sim":
    user_atual = utils.valida_admin()
    if type(user_atual) == bool:
      exit()
    else:
      print(f"\nSeja bem-vindo, {user_atual}.\n")
    cadastro_produtos = utils.cadastra_produtos()
    exit()
elif admin.lower != "sim":
    user_atual = utils.valida_usuario()

if type(user_atual) == bool:
  exit()
else:
  print("-------------------------------------------------")
  print("| ***---- SEJA BEM-VINDO ", user_atual ,"---- *** |")

  carrinho = []

  while True:
    produtos = open("arquivos/produtos.txt", "r").readlines()

    print("Esses são nossos produtos disponíveis em estoque, caso queria cancelar o processo de compra, digite: SAIR")
    for indice, prod in enumerate(produtos):
      print("| ***---- ", indice, prod.split(";")[0] + " - R$", prod.split(";")[1].replace("\n", ""),   "---- *** |")
    print("-------------------------------------------------")

    escolha = input("Digite o número do produto que deseja comprar ou SAIR: ")

    if "SAIR" == escolha.upper():
      break
    try:    
      print("Você escolheu o produto: ", produtos[int(escolha)].split(";")[0], " - R$ ", produtos[int(escolha)].split(";")[1].replace("\n", ""))
    except:
      print("####### Digite um número válido! ######")
      continue
    adicionar = input("Deseja adicionar ao carrinho? S/N ")

    if adicionar.upper() == "S":
      qtde = int(input("Qual a quantidade que deseja adicionar? "))
      if qtde <= 0:
        print("Digite uma quantidade maior que 0")
        continue
      
      preco_produto = produtos[int (escolha)].split(";")[1].replace("\n","")
      carrinho.append([produtos[int(escolha)].split(";")[0],preco_produto, round(float(preco_produto) * qtde, 2), qtde])

  if len(carrinho) > 0:
    vr_total = 0
    for indice, produto in enumerate(carrinho):
      print(f"{indice+1} | Nome: {produto[0]} | Qtde: {produto[-1]} | Preço: R${produto[1]} | Vr Total: R${produto[2]}")
      vr_total += produto[2]
    print(f"\n############ VALOR TOTAL: R${round(vr_total,2)}")
    print("\nSalvando arquivo de orçamento. Obrigado por comprar conosco!")

  print("\nIremos redirecioná-lo para a sessão de pagamento.")
  escolha = input("Qual será a forma de pagamento? Pix ou cartão de crédito? ")
  if escolha.lower() == "pix":
    print(f"O total a pagar será R${round(vr_total),2}. Utilize a chave pix a seguir para realizar o pagamento: 53200970855")
  elif escolha.lower != "pix":
    cartao = utils.cartao_credito()
    print(f"A compra no valor de R${round(vr_total,2)} foi realizada com sucesso!!!")
  else:
    print("Digite uma escolha válida!!!")
    exit()
