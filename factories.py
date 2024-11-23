

# Archivo: factories.py

class ProductFactory:
    @staticmethod
    def create_fake_product():
        # Aquí simulamos la creación de un producto falso con valores predeterminados
        return {
            "id": 1,
            "name": "Producto Falso",
            "price": 10.99,
            "category": "Falsos",
            "availability": True
        }
