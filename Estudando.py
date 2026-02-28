linhas = [
    "SISTEMA: iniciado com sucesso",
    "ERRO: falha na conexão com o banco",
    "USUARIO: login realizado",
    "ERRO: senha incorreta",
    "SISTEMA: atualização concluída",
    "ERRO: tempo de resposta excedido",
    "USUARIO: logout realizado"
]

x = 0
for frase in linhas:
    if "ERRO" in frase:
            x+=1

print(f"Total de erros: {x}")
