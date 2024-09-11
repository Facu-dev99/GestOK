import tkinter as tk
from tkinter import messagebox
from productManager import Product
from cartManager import Cart

class GestOKApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GestOK - Gestión de Carrito")
        self.cart = Cart()

        self.label = tk.Label(root, text="Gestión de Carrito", font=("Arial", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(root, text="Nombre del producto:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.price_label = tk.Label(root, text="Precio del producto:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.quantity_label = tk.Label(root, text="Cantidad:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Agregar producto", command=self.add_product)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Quitar producto", command=self.remove_product)
        self.remove_button.pack(pady=5)

        self.show_cart_button = tk.Button(root, text="Ver carrito", command=self.show_cart)
        self.show_cart_button.pack(pady=5)

        self.clear_cart_button = tk.Button(root, text="Vaciar carrito", command=self.clear_cart)
        self.clear_cart_button.pack(pady=5)

        self.total_button = tk.Button(root, text="Calcular total", command=self.total_cart)
        self.total_button.pack(pady=5)

        self.receipt_button = tk.Button(root, text="Imprimir recibo", command=self.print_receipt)
        self.receipt_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Salir", command=root.quit)
        self.exit_button.pack(pady=10)

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        if not name or not price or not quantity:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        try:
            price = int(price)
            quantity = int(quantity)
            product = Product(name, price)
            self.cart.add_product(product, quantity)
            messagebox.showinfo("Éxito", f"Producto '{name}' agregado con éxito.")
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números válidos.")

    def remove_product(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showerror("Error", "Debe ingresar el nombre del producto a eliminar.")
            return

        product_to_remove = None
        for product in self.cart.items.keys():
            if product.name == name:
                product_to_remove = product
                break

        if product_to_remove:
            try:
                quantity = int(self.quantity_entry.get() or 1)
                self.cart.remove_product(product_to_remove, quantity)
                messagebox.showinfo("Éxito", f"Producto '{name}' eliminado con éxito.")
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número válido.")
        else:
            messagebox.showerror("Error", f"El producto '{name}' no está en el carrito.")

    def show_cart(self):
        cart_items = "\n".join([f'{product.name} (x{quantity}) - ${product.price}' 
                            for product, quantity in self.cart.items.items()])
        if not cart_items:
            cart_items = "El carrito está vacío."
        messagebox.showinfo("Carrito", cart_items)

    def clear_cart(self):
        self.cart.clear_cart()
        messagebox.showinfo("Éxito", "El carrito se ha vaciado con éxito.")

    def total_cart(self):
        total = self.cart.total_cart()
        messagebox.showinfo("Total", f"El total del carrito es: ${total}")

    def print_receipt(self):
        receipt = "\n".join([f'{product.name} (x{quantity}) - ${product.price}' 
                            for product, quantity in self.cart.items.items()])
        total = self.cart.total_cart()
        receipt += f"\nTotal: ${total}"
        messagebox.showinfo("Recibo", receipt)

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestOKApp(root)
    root.mainloop()
