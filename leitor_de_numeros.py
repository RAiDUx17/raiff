tentativas = 5
def leitor_de_numeros():
    soma = 0
    lista = []
    qtd = 0
    maior = None
    menor = None
    limite = 5
    cont_par = 0
    cont_imp = 0

    while True:
        if limite == 0:
            print("limite excedido")
            break
        else:
            try:
                numero = int(input("digite um numero:"))
            except ValueError:
                print("digite um numero valido")
                limite -= 1
                continue

        if numero == 0:
            if qtd > 0:
                media = soma / qtd
            else:
                media = 0
            print(f"lista de numero: {lista}")
            print(f"foram digitados {qtd} numeros")
            print(f"a soma do numeros e: {soma}")
            print(f"a media de numeros e: {media}")
            print(f"o maior numero foi: {maior}")
            print(f"o menor numero foi: {menor}")
            print(f"total de numeros pares: {cont_par}")
            print(f"total de numeros imopares: {cont_imp}")
            break
        else:

            lista.append(numero)
            soma += numero
            qtd += 1
            if numero % 2== 0:
                cont_par +=1
            else:
                cont_imp += 1
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero

while True:
    if tentativas == 0:
        print("limite excedido")
        break
    else:

        try:
            print("\nMenu")
            print('1.Ler numeros')
            print("2.Fechar programa")
            opcao = int(input("escolha uma opcao: "))
        except ValueError:
            print("escolha uma opcao valida")
            tentativas -= 1
            continue

    if opcao > 2:
        print("escolha uma opcao valida")
        tentativas -= 1
    elif opcao < 1:
        print("escolha uma opcao valida")
        tentativas -= 1

    elif opcao == 1:
        leitor_de_numeros()
    else:
        print("obrigado por usar o programa")
        break

