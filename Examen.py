productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {
    '8475HD': [387990, 10], 
    '2175HD': [327990, 4], 
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], 
    '123FHD': [290890, 32], 
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 
    'UWU131HD': [349990, 1], 
    'FS1230HD': [249990, 0], 
}

def stock_marca(marca):
    stock_disponible = 0
    for Clave, Valor in productos.items():
        if marca == Valor[0]:
            for clave, valor in stock.items():
                if Clave == clave:
                    stock_disponible += valor[1]
    if stock_disponible > 0:
        print('El stock es: ', stock_disponible)
    else:
        return None

def busqueda_precio(p_min, p_max):
    precio_productos = []
    while True:
        for Clave, Valor in stock.items():
            for clave, valor in productos.items():
                precio = Valor
                if precio < 0:
                    print('No hay notebooks en ese rango de precios')
                    return
                elif p_min < precio and p_max < precio:
                    precio_productos.append[valor[0], clave]
                    print('Los nootebooks entre los precios consultados son: ', precio_productos)
                    break
                else: 
                    print('Debe ingresar valores enteros!!')

def ordenar_productos():
    print('------Listado de Notebooks Ordenado------')
    for clave, valor in productos.items():
        print(f'{valor[0]}-{clave}-{valor[2]}-{valor[3]}-{valor[4]}') 

while True:
    print('***MENU PRINCIPAL***')
    print('1. Stock marca.')
    print('2. Busqueda por precio.')
    print('3. Listado de productos')
    print('4. Salir')
    
    opc = input('Ingrese que opcion: ')
    
    if opc == '1':
        marca = input('Ingrese marca a consultar: ')
        stock_marca(marca)
    elif opc == '2':
        p_min = input('Ingrese precio minimo: ')
        p_max = input('Ingrese precio maximo: ')
        busqueda_precio(p_min, p_max)
    elif opc == '3':
        ordenar_productos()
    elif opc == '4':
        print('Programa finalizado')
        break
    else:
        print('Debe seleccionar una opcion valida!!')
