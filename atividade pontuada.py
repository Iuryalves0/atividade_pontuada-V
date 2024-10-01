import os
import time
from  dataclasses import dataclass
os.system("cls||clear")

#definindo listas e variaveis
qtd_familias = 0
lista_de_familias = []
lista_salarios = []
         
#aparecer as opções
def menu_opçoes():
    print("""
codigo| Descrição
  1   | Adicionar familia
  2   | Exibir resultados
  3   | sair
      """)
    

while True:
    os.system("cls||clear")

    menu_opçoes() #chamando variavel para aparição do menu
    opcao = input("Escolha uma das 3 opções no menu: ")
    match opcao:
        case "1": 
                os.system("cls||clear")
                qtd_familias += 1
                
               #solicitando dados
                qntd_filhos = int(input("Informe sua quantidade de filhos: "))
                qntd_salarios = int(input("Escreva quantos salários você possui: "))
                salarios = []  # Usando uma lista temporária para armazenar salários

                for i in range(qntd_salarios):
                    salario = float(input(f"Digite qual o {i+1} seu salário: "))
                    salarios.append(salario)
                
                media_salarial = sum(salarios) / qtd_familias
                maior_salario = max(salarios) 
                menor_salario = min(salarios)
                media_filhos = qntd_filhos / qtd_familias
                
        case "2": 
            os.system("cls||clear")
            print("==== Exibindo resultados ====")
            print(f"\n numero de familias que responderam a pesquisa: {qtd_familias}")
            print(f"media do salario da população: {media_salarial}")
            print(f"media do numero de filhos: {media_filhos}")
            print(f"maior salario: {maior_salario}")
            print(f"menor salario: {menor_salario}")
            break

        case "3": 
            print("Saindo do programa...")
            time.sleep(3)
            break