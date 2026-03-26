# Envio do Sal

Sal administra a maior empresa de transportes da região metropolitana, a Sal's Shippers. Ele quer garantir que cada um de seus clientes tenha a melhor e mais acessível experiência no envio de suas encomendas.

Neste projeto, você criará um programa que receberá o peso de um pacote e determinará a maneira mais barata de enviá-lo usando o serviço de entrega Sal's Shippers.

A Sal's Shippers oferece diversas opções para que o cliente envie sua encomenda:

- Envio terrestre, que consiste em uma pequena taxa fixa mais uma taxa baseada no peso do seu pacote.
- Envio Terrestre Premium é uma opção com taxa fixa bem mais alta, mas não cobrada com base no peso.
- Envio por drones (novidade), que não possui taxa fixa, mas o valor baseado no peso é o triplo do valor do envio terrestre.

## Tabela de Preços

| Tipo de Envio | Peso da Embalagem | Preço por Libra | Taxa Fixa |
|---|---|---|---|
| Terrestre | 2 libras ou menos | $1,50 | $20,00 |
| Terrestre | Mais de 2 até 6 libras | $3,00 | $20,00 |
| Terrestre | Mais de 6 até 10 libras | $4,00 | $20,00 |
| Terrestre | Mais de 10 libras | $4,75 | $20,00 |
| Terrestre Premium | Qualquer peso | — | $125,00 |
| Drones | 2 libras ou menos | $4,50 | $0,00 |
| Drones | Mais de 2 até 6 libras | $9,00 | $0,00 |
| Drones | Mais de 6 até 10 libras | $12,00 | $0,00 |


Escreva um programa em Python chamado shipping.py que receba o peso de um pacote e calcule qual o método de envio mais barato e quanto custará o envio usando a Sal's Shippers.