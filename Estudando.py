#from collections import Counter


# linhas = [
#     "SISTEMA: iniciado com sucesso",
#     "ERRO: falha na conexão com o banco",
#     "USUARIO: login realizado",
#     "ERRO: senha incorreta",
#     "SISTEMA: atualização concluída",
#     "ERRO: tempo de resposta excedido",
#     "USUARIO: logout realizado"
# ]

# categorias = {
#     "ERRO": [],
#     "SISTEMA": [],
#     "USUARIO": []
# }


# for frase in linhas:
#     if "ERRO" in frase:
#           categorias["ERRO"].append(frase)

#     elif "USUARIO" in frase:
#          categorias["USUARIO"].append(frase)

#     elif "SISTEMA" in frase:
#          categorias["SISTEMA"].append(frase)

# print(
#      f"Total de erros: {len(categorias['ERRO'])}\n"
#      f"{categorias['ERRO']}\n"
#      f"Total de usuários: {len(categorias['USUARIO'])}\n"
#      f"{categorias['USUARIO']}\n"
#      f"Total de sistemas: {len(categorias['SISTEMA'])}\n"
#      f"{categorias['SISTEMA']}"
#      )

# linhas = [
#     "SISTEMA: iniciado com sucesso",
#     "ERRO: falha na conexão com o banco",
#     "USUARIO: login realizado",
#     "ERRO: senha incorreta",
#     "SISTEMA: atualização concluída",
#     "ERRO: tempo de resposta excedido",
#     "USUARIO: logout realizado"
# ]

# dicionario = {}

# for frase in linhas:
#         chave, valor = frase.split(":")
#         valor = valor.strip()

#         if chave not in dicionario:
#                 dicionario[chave] = []

#         dicionario[chave].append(valor)

# print(dicionario)


# alimento = [
#     "FRUTA: maçã",
#     "LEGUME: cenoura",
#     "FRUTA: banana",
#     "BEBIDA: água",
#     "FRUTA: uva",
#     "LEGUME: batata"
# ]

# dicionario = {}

# for frase in alimento:
#     chave, valor = frase.split(":")
#     valor = valor.strip()

#     if chave not in dicionario:
#         dicionario[chave] = []

#     dicionario[chave].append(valor)

# print(dicionario)



# registros = [
#     "João,Matemática",
#     "Maria,Português",
#     "João,História",
#     "Ana,Matemática",
#     "Maria,História",
#     "João,Matemática",
#     "Ana,Português"
# ]

# dicionario = {}

# for frase in registros:
#     chave, valor = frase.split(",")
#     valor = valor.strip()
#     dicionario[chave] = dicionario.get(chave, 0)+1
        
#     if chave not in dicionario:
#         dicionario[chave] = []
    
# print(dicionario)





