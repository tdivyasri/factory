# Archivo: test_routes.py

import unittest
from flask import Flask
from flask_testing import TestCase

from app import app  # Importa tu aplicación Flask

class TestRoutes(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_leer_producto(self):
        # Subprueba 3a - Leer
        response = self.client.get('/productos/1')
        self.assertEqual(response.status_code, 200)  

    def test_actualizar_producto(self):
        # Subprueba 3b - Actualizar
        response = self.client.put('/productos/1', json={'nombre': 'Nuevo Nombre'})
        self.assertEqual(response.status_code, 200)  

    def test_borrar_producto(self):
        # Subprueba 3c - Borrar
        response = self.client.delete('/productos/1')
        self.assertEqual(response.status_code, 200)  

    def test_listar_todo(self):
        # Subprueba 3d - Listar Todo
        response = self.client.get('/productos')
        self.assertEqual(response.status_code, 200)  

    def test_listar_por_nombre(self):
        # Subprueba 3e - Listar por Nombre
        response = self.client.get('/productos?nombre=AlgunNombre')
        self.assertEqual(response.status_code, 200)  

    def test_listar_por_categoria(self):
        # Subprueba 3f - Listar por Categoría
        response = self.client.get('/productos?categoria=AlgunaCategoria')
        self.assertEqual(response.status_code, 200)  

    def test_listar_por_disponibilidad(self):
        # Subprueba 3g - Listar por Disponibilidad
        response = self.client.get('/productos?disponible=true')
        self.assertEqual(response.status_code, 200)  

if __name__ == '__main__':
    unittest.main()
