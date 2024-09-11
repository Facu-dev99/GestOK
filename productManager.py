from database import create_connection

class Product:
    def __init__(self, name, price = None):
        self.name = name
        self.price = price

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (self.name, self.price))
        conn.commit()
        conn.close()


