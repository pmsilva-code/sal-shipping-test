def envio_terrestre():

    print("- SEJA BEM VINDO AO ENVIO TERRESTRE -")
    lb = float(input("Digite o peso do pacote em libras: "))
    price_per_pound = float(input("Digite o preço por libra: "))
    flat_charge = 20.00
    cost_package = lb * price_per_pound + flat_charge
    cost_package_ground_shipping = 125.00

    # Envio terrestre:
    if lb <= 2:
        price_per_pound = 1.50
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 0 á 2 libras, o preço é de $1,50"
        )
        print(f"O custo total do pacote é de ${cost_package:.2f}")
        print(
            f"O custo total do pacote com frete terrestre premium é de ${cost_package_ground_shipping:.2f}"
        )
        print("*" * 30)
    elif lb > 2 and lb <= 6:
        price_per_pound = 3.00
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 2 á 6 libras, o preço é de $3,00"
        )
        print(f"O custo total do pacote é de ${cost_package:.2f}")
        print(
            f"O custo total do pacote com frete terrestre premium é de ${cost_package_ground_shipping:.2f}"
        )
        print("*" * 30)
    elif lb > 6 and lb <= 10:
        price_per_pound = 4.00
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 6 á 10 libras, o preço é de $4,00"
        )
        print(f"O custo total do pacote é de ${cost_package:.2f}")
        print(
            f"O custo total do pacote com frete terrestre premium é de ${cost_package_ground_shipping:.2f}"
        )
        print("*" * 30)
    elif lb > 10:
        price_per_pound = 4.75
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 12 á 20 libras, o preço é de $4.75"
        )
        print(f"O custo total do pacote é de ${cost_package:.2f}")
        print(
            f"O custo total do pacote com frete terrestre premium é de ${cost_package_ground_shipping:.2f}"
        )
        print("*" * 30)


def envio_por_drone():
    print("- SEJA BEM VINDO AO ENVIO POR DRONE -")
    lb = float(input("Digite o peso do pacote em libras: "))
    price_per_pound = float(input("Digite o preço por libra: "))
    flat_charge = 0.00
    cost_package = lb * price_per_pound + flat_charge

    # Envio por Drone:
    if lb <= 2:

        price_per_pound = 4.50
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 0 á 2 libras, o preço é de $4,50"
        )
        print(f"O custo total do pacote por envio por drone é de ${cost_package:.2f}")
        print("*" * 30)

    elif lb > 2 and lb <= 6:
        price_per_pound = 9.00
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 2 á 6 libras, o preço é de $9,00"
        )
        print(f"O custo total do pacote por envio por drone é de ${cost_package:.2f}")
        print("*" * 30)

    elif lb > 6 and lb <= 10:
        price_per_pound = 12.00
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 6 á 10 libras, o preço é de $12,00"
        )
        print(f"O custo total do pacote por envio por drone é de ${cost_package:.2f}")
        print("*" * 30)

    elif lb > 10:
        price_per_pound = 14.25
        print("*" * 30)
        print(
            "O peso do pacote esta na classificação de 12 á 20 libras, o preço é de $14,25"
        )
        print(f"O custo total do pacote por envio por drone é de ${cost_package:.2f}")
        print("*" * 30)


envio_terrestre()
envio_por_drone()
