import unittest

def soma(a, b):
    """Função simples que retorna a soma de dois números."""
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

# Para rodar dentro de ambientes como Jupyter ou Colab
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSoma)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
