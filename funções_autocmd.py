import os
import socket

def list_dir_atual() -> str:
    return f"Diretório atual: {os.getcwd()}"

def list_dir (nome_dir):
    try:
        dir=os.listdir(nome_dir)
        return dir
    except FileNotFoundError:
        return(f'Erro! o arquivo/diretório não pode ser encontrado')
    except PermissionError:
        return(f'você nâo tem permissão para acessar')
    
def mudar_diretorio(novo_dir: str) -> str:
    try:
        os.chdir(novo_dir)
        return f"Mudou para o diretório: {os.getcwd()}"
    except Exception as e:
        return f"Erro: {str(e)}"

def criar_diretorio(nome_dir: str) -> str:
    try:
        os.mkdir(nome_dir)
        return f"Diretório {nome_dir} criado com sucesso!"
    except Exception as e:
        return f"Erro: {str(e)}"

def renomear(dir_antigo,dir_novo):
    try:
        os.rename(dir_antigo, dir_novo)
        return f"'{dir_antigo}' foi renomeado para '{dir_novo}' com sucesso!"
    except FileNotFoundError:
        return f"Erro: '{dir_antigo}' não encontrado!"
    except PermissionError:
        return f"Erro: Permissão negada para modificar '{dir_antigo}'!"
    except FileExistsError:
        return f"Erro: '{dir_novo}' já existe!"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def tree(dir):
    dir=input('digite o nome do diretório')