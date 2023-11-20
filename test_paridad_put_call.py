

import unittest
from paridad_put_call import ParidadPutCall


class TestParidadPutCall(unittest.TestCase):
    def setUp(self):
        # Initialize SinteticoMaker instance
        self.Paridad = ParidadPutCall()

    def test_calculate_call_price(self):
        put = 6.639993438941417
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = (24.090000000000003)

        result = self.Paridad.calculate_call_price(put, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_calculate_put_price(self):
        call = 24.090000000000003
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = (6.639993438941417)

        result = self.Paridad.calculate_put_price(call, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_is_parity(self):
        call = 24.090000000000003
        put = 6.639993438941417
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = (True)

        result = self.Paridad.is_parity(call, put, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_calculate_limite_inferior_call(self):
        S = 28
        K = 25
        r = 0.06
        T = 0.33
        expected_result = 3.49

        result = self.Paridad.calculate_limite_inferior_call(S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_calculate_limite_inferior_put(self):
        S = 12
        K = 15
        r = 0.06
        T = 0.33
        expected_result = 2.71

        result = self.Paridad.calculate_limite_inferior_put(S, K, r, T)

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
