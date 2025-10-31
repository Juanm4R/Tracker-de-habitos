import unittest
from main import calcular_racha, premio_por_progreso, calcular_porcentajes_lambda

class TestTracker(unittest.TestCase):

    def test_calcular_racha(self):
        racha_actual, racha_maxima = calcular_racha([1, 1, 0, 1, 1, 1])
        self.assertEqual(racha_actual, 3)
        self.assertEqual(racha_maxima, 3)

    def test_premio_por_progreso(self):
        # Solo se verifica que no tire error
        premio_por_progreso("Ejercicio", 3, 4)
        self.assertTrue(True)

    def test_calcular_porcentajes_lambda(self):
        habitos = [["Ejercicio", [1, 1, 0, 1]], ["Leer", [0, 0, 1, 1, 1]]]
        calcular_porcentajes_lambda(habitos)
        self.assertTrue(True)  # solo verifica ejecución sin errores

if __name__ == "__main__":
    unittest.main()