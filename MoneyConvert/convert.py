def exchange(currency, quantity):
    result = 0
    # Rubles
    if currency == 1:
        result = quantity * 0.014
        print(f'{quantity}₽ are ${result} USD')
    # Colombian pesos
    elif currency == 2:
        result = quantity * 0.00027
        print(f'${quantity} COP are ${result} USD')
    # Moneda mexicana
    elif currency == 3:
        result = quantity * 0.044
        print(f'${quantity} MEX are ${result} USD')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')


try:
    currency = int(input('''
    Chose currency:
    [1] Rubles 
    [2] Colombian Pesos
    [3] Mexican Pesos
    '''))
    print("-----------------------")
    quantity = float(input("Quantity: "))
    exchange(currency, quantity)
except OSError as err:
    print("Error")
    print("Please, type numeric values")
