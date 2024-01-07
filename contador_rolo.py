import copy

# Criando as váriaveis
rolos = []
OPs = []
cont = 0
tot_op = 0
tot_rolo = 0

# Faz um loop
resp1 = ""
while resp1.upper() != "N":
    # Pede ao usuário para inserir quantas ops sera dada entrada
    ent_op = int(input("Digite a quantidade de OPs: "))
    tot_op += ent_op

    # Faz um laço perguntando as ops
    for op in range(ent_op):
        elemento = input("Digite a OP: ")
        OPs.append(elemento)
        total = 0

        # Faz um laço adicionando os rolos em uma lista
        resp2 = ""
        while resp2.upper() != "N":
            elemento = input("Digite a quantidade de rolos: ")
            total += int(elemento)
            cont += 1

            # Pergunta se quer finalizar o laço
            print()
            resp2 = input("Deseja adicionar mais? S/N ")
            print()

        # Adiciona o total na lista
        ent_rolo = [total]
        tot_rolo += total
        rolos.append(ent_rolo.copy())

    # Exibe a lista final
    for c in range(tot_op):
        print(f"{OPs[c]} / {rolos[c][0]}")
    print(f"TOTAL= {tot_rolo}")

    if cont >= 1:
        # Pergunta se quer finalizar o código
        print()
        resp1 = input("Deseja continuar a contagem? S/N ")
        print()
print("FINALIZADO!")
