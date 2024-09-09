from cartManager import Cart
from productManager import Product

cart = Cart()

print(':::::::::::::::::::::::::::::::::')
print('... .: Bienvenid@ a GestOK :. ...')
print(':::::::::::::::::::::::::::::::::\n')


while True :

    print(':::::::::::::::::::::::::::::::::')
    print('[1] ... Agregar producto ........')
    print('[2] ... Quitar producto .........')
    print('[3] ... Ver carrito .............')
    print('[4] ... Vaciar carrito ..........')
    print('[5] ... Calcular total ..........')
    print('[6] ... Imprimir recibo .........')
    print('[7] ... Salir ...................')

    user_input = int(input('\n Seleccione la operacion que desea realizar: '))

    if user_input == 1:

        name = str(input('\n.: Inserte el nombre del producto: '))
        price = int(input('\n.: Inserte el precio del producto: $'))
        quantity = int(input('\n.: Inserte la cantidad del producto: '))

        product = Product(name, price)
        cart.add_product(product,quantity)

    elif user_input == 2:
        name = str(input('\n.: Inserte el nombre del producto a eliminar: '))
        
        product_to_remove = None
        for product in cart.items.keys():
            if product.name == name:
                product_to_remove = product
                break

        if product_to_remove:
            quantity = int(input('\n.: Inserte la cantidad del producto a eliminar (por defecto 1): '))
            cart.remove_product(product_to_remove, quantity)
        else:
            print('\n::::::::::::::::::::::::::::::::\n')
            print(' El producto no está en el carrito. ')
            print('\n::::::::::::::::::::::::::::::::\n')

    elif user_input == 3:

        cart.show_cart()

    elif user_input == 4:

        cart.clear_cart()
        print('\n::::::::::::::::::::::::::::::::\n')
        print(' El carrito se ha vaciado con exito.')
        print('\n::::::::::::::::::::::::::::::::\n')

    elif user_input == 5:

        cart.total_cart()

    elif user_input == 6:

        cart.print_recepit()

    elif user_input == 7:

        print('\n:::::::::::::::: Saliendo... ::::::::::::::::\n')

        break

    else:
        
        print('\n:::::::::::::::: ¡ ATENCIÓN ! ::::::::::::::::\n')
        print('Operación invalida. Intente nuevamente.')
        print('\n::::::::::::::::::::::::::::::::::::::::::::::\n') 







