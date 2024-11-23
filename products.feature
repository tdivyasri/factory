# Archivo: products.feature

Feature: Manejo de productos
  Escenario: Leer un producto existente
    Given I have a product with ID 1
    When I request the product with ID 1
    Then I receive the product details

  # Otros escenarios para Actualización, Borrado, Búsqueda por Nombre, Categoría, Disponibilidad, etc.
