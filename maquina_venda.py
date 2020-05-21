moedas = 0
total = 0
lista = []

print("Bem vindo a máquina de refrigerantes")
print("A máquina aceita apenas moedas de $0.10 e $0.25 ")

for numero in range(3):
    moedas = (int(input("Insira as moedas: ")))
    if moedas == 25 or moedas == 10:
        """Inserindo os valores do usuario na lista"""
        lista.append(moedas)
    else:
        print("A máquina não aceita essa moeda")
        break

"""Soma e Imprime os valores da lista"""
total = sum(lista)
print(f'moedas {lista}')
print(f'Total {total}')

def retorna_coca(total):
    if total == 45:
        return "Coca Cola"
    else:
        return "Você inseriu o valor errado"

print(retorna_coca(total))
