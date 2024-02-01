Tienda = {'camisas':50000,'figuras':20000,'katanas':70000,'dakimakuras':200000}

print('Bienvenido a nuestra tienda anime')
print('los productos en venta mas pedidos son: ')
print(Tienda)

prod = str(input('ingrese el nombre del producto a comprar: '))

if prod == 'camisas' or 'camisas' or 'camisas':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['camisas']* cant) 
    print('Gracias por la compra de la camisa, que tenga un buen dia')

elif prod == 'figuras' or 'figuras' or 'muñecos' or 'muñecos':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['figuras']* cant) 
    print('Gracias por la compra de nuestras figuras, que tenga un buen dia')

elif prod == 'katanas' or 'katanas' or 'katanas' or 'katanas' or 'espadas' or 'samurais':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['katanas']* cant) 
    print('Gracias por la compra de la katana, que tenga un buen dia')

elif prod == 'dakimakuras' or 'dakimakuras' or 'dakimakuras' or 'almohadas':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print (Tienda['dakimakuras']* cant) 
    print('Gracias por la compra de su nueva dakimakura, que tenga un buen dia')

else:
    print('Actualmente no contamos con stock para el producto ', prod, ', vuelva después para revisarlo.')