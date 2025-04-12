import os
import socket
import funções_autocmd as cmd

while True:
    comando = input('\nO que você gostaria de fazer?\n'
                    '1 - Entrar em um diretório\n'
                    '2 - Criar um diretório\n'
                    '3 - Listar um diretório\n'
                    '4 - Ver o diretório atual\n'
                    '5 - Renomear um diretório\n'
                    '6 - Sair\n'
                    'Opção: ')

    if comando == '1':
        diretorio = input("Digite o caminho do diretório (se quiser voltar digite ..): ")
        print(cmd.mudar_diretorio(diretorio))
    
    elif comando == '2':
        nome = input("Digite o nome do novo diretório: ")
        print(cmd.criar_diretorio(nome))
    
    elif comando == '3':
        nome_dir = input('coloque o nome do diretório desejado: ')
        print(cmd.list_dir(nome_dir))
    
    elif comando == '4':
        print(cmd.list_dir_atual())
    
    elif comando == '5':
        dir_antigo = input('Digite o nome original: ').strip()
        dir_novo = input('Digite o novo nome: ').strip()
        print(cmd.renomear(dir_antigo, dir_novo)) 
    
    elif comando == '6':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")