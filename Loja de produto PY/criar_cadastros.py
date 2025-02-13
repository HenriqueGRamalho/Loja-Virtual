import utils

print("Bem-vindo a nossa plataforma de cadastros! ")
escolha = input("\nVocê deseja cadastrar um usuário(user) ou administrador(admin)? ")

if escolha.lower == "admin":
    cadastro = utils.cadastra_admin()
else:
    cadastro = utils.cadastra_usuario()