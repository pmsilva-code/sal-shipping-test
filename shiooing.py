def table_terrestre():

    lb = float(input("Digite o peso do pacote em libras: "))
    price_per_pound = float(input("Digite o preço por libra: "))
    flat_charge = 20.00
    cost_package = lb * price_per_pound + flat_charge

    # Envio terrestre:
    if lb <= 2:
        price_per_pound = 1.50
        print("*" * 30)
        print("O peso do pacote é de 2 libras, o preço é de $4,50")
        print(f"O custo total do pacote é de ${cost_package:.2f}")
    elif lb < 2 or lb == 6:
        price_per_pound = 3.00
        print("*" * 30)
        print("O peso do pacote é de 9 libras, o preço é de $9,00")
        print(f"O custo total do pacote é de ${cost_package:.2f}")
    elif lb > 6 and lb <= 10:
        price_per_pound = 1.20
        print("*" * 30)
        print("O peso do pacote é de 20 libras, o preço é de $12,00")
        print(f"O custo total do pacote é de ${cost_package:.2f}")
    elif lb > 10:
        price_per_pound = 2.00
        print("*" * 30)
        print("O peso do pacote é de 20 libras, o preço é de $20,00")
        print(f"O custo total do pacote é de ${cost_package:.2f}")


table_terrestre()
