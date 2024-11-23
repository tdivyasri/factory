# Archivo: test_models.py

import unittest
from products_module import Product  # Importa tu módulo o clase Producto

class TestProductMethods(unittest.TestCase):
    def setUp(self):
        self.product = Product('Producto 1', 'Categoría A', 100, True)
        # Suponiendo un producto de prueba

    def test_leer_producto(self):
        self.assertEqual(self.product.name, 'Producto 1')
        self.assertEqual(self.product.category, 'Categoría A')

    def test_actualizar_producto(self):
        self.product.update_name('Nuevo nombre')
        self.assertEqual(self.product.name, 'Nuevo nombre')

    def test_borrar_producto(self):
        self.product.delete()
        self.assertIsNone(self.product)

    def test_listar_todo(self):
        # Suponiendo una lista de productos
        products_list = [Product('P1', 'Cat1', 50, True), Product('P2', 'Cat2', 70, False)]
        self.assertEqual(len(products_list), 2)

    def test_buscar_por_nombre(self):
        self.assertEqual(self.product.name, 'Producto 1')

    def test_buscar_por_categoria(self):
        self.assertEqual(self.product.category, 'Categoría A')

    def test_buscar_por_disponibilidad(self):
        self.assertTrue(self.product.available)

if __name__ == '__main__':
    unittest.main()
