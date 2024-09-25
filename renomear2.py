import os
# para criar uma função python iremos utilizar o comando
# def(definição)
def mudarNome(ar_or,nv_ar):
    """
    A função mudarNome, altera o nome de um arquivo.
    O usuário deve passar o nome original do arquivo e
    o novo nome.
    Args:
        ar_or (str): O nome original do arquivo
        nv_ar (str): O novo nome do arquivo
    Returns:
        Retorna uma mensagem de confirmação
    """
    os.rename(ar_or,nv_ar)
    msg = "O nome do arquivo foi alterado"
    return msg 

arquivo_original = input("Digite o nome do arquivo que será renomeado")
novo_arquivo = input("Digite o novo nome do arquivo")
rs = mudarNome(arquivo_original, novo_arquivo)
print (rs)