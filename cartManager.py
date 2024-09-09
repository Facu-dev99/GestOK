class Cart :
    def __init__(self):
        self.items = {}

    #Añadir producto
    def add_product (self, product, quantity = 1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        print('\n::::::::::::::::::::::::::::::::\n')
        print(f'\n+ {quantity} unidade(s) de {product.name} agregado(s) al carrito.\n')
        print('\n::::::::::::::::::::::::::::::::\n')

    #Quitar producto
    def remove_product(self, product, quantity=1):

        if product in self.items:

            if self.items[product] > quantity:

                self.items[product] -= quantity

                print('\n::::::::::::::::::::::::::::::::\n')
                print(f'- {quantity} unidade(s) de {product.name} eliminada(s) del carrito.')
                print('\n::::::::::::::::::::::::::::::::\n')

            elif self.items[product] == quantity:

                del self.items[product]

                print('\n::::::::::::::::::::::::::::::::\n')
                print(f'- {quantity} unidade(s) de {product.name} eliminada(s). El producto ha sido eliminado completamente del carrito.')
                print('\n::::::::::::::::::::::::::::::::\n')

            else:

                print('\n::::::::::::::::::::::::::::::::\n')
                print(f'No hay suficientes unidades de {product.name} para eliminar.')
                print('\n::::::::::::::::::::::::::::::::\n')

        else:

            print('\n::::::::::::::::::::::::::::::::\n')
            print(f'{product.name} no está en el carrito.')
            print('\n::::::::::::::::::::::::::::::::\n')

    #Ver carrito
    def show_cart(self):

        if not self.items:
            print('\n::::::::::::::::::::::::::::::::\n')
            print(' El carrito esta vacio. ')
            print('\n::::::::::::::::::::::::::::::::\n')
        else:
            print('\n::::::::::::::::::::::::::::::::\n')
            print(' PRODUCTOS EN EL CARRITO : ')
            print('\n::::::::::::::::::::::::::::::::\n')

            for product, quantity in self.items.items():
                print(f" · {product.name}: {quantity} unidad(es) - Precio unitario: ${product.price}\n")

    #Vaciar carrito
    def clear_cart(self):
        self.items.clear()

    #Calcular total
    def total_cart(self):
        total_calc = sum(product.price * quantity for product, quantity in self.items.items())
        print('\n::::::::::::::::::::::::::::::::\n')
        print(f'Total en carrito: ${total_calc}')
        print('\n::::::::::::::::::::::::::::::::\n')

        return total_calc

    #Facturacion
    def print_recepit(self):
        total_calc = sum(product.price * quantity for product, quantity in self.items.items())
        print('\n:::::::::::::: RECIBO DE COMPRA :::::::::::::::::\n')
        item_info = "\n".join(f"{product.name}: {quantity} x ${product.price} = ${product.price * quantity}"
                            for product, quantity in self.items.items())
        print('\n:::::::::::::::::::::::::::::::::::::::::::::::::\n')
        print(f"{item_info}\n", f"\nTotal: ${total_calc}")
        print('\n...................................................\n')

