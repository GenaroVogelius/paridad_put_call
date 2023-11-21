

import unittest
from paridad_put_call import ParidadPutCall


class TestParidadPutCall(unittest.TestCase):
    def setUp(self):
        # Initialize SinteticoMaker instance
        self.Paridad = ParidadPutCall()

    def test_call_sint_long(self):
        put = 6.639993438941417
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = (24.090000000000003)

        result = self.Paridad.call_sint_long(put, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_put_sint_long(self):
        call = 24.090000000000003
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = (6.639993438941417)

        result = self.Paridad.put_sint_long(call, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_call_sint_short(self):
        S=40; 
        K=42; 
        put=4; 
        T=30/365; 
        r= 0.30
        expected_result= -3.0229528621658233
        result = self.Paridad.call_sint_short(put, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_put_sint_short(self):
        S=40; 
        K=42; 
        call=2; 
        T=30/365; 
        r= 0.30
        expected_result= -2.9770471378341767
        result = self.Paridad.put_sint_short(call, S, K, r, T)

        self.assertEqual(result, expected_result)

    def test_is_parity(self):
        call = 24.090000000000003
        put = 6.639993438941417
        S = 200
        K = 190
        r = 0.2
        T = 0.2
        expected_result = ("Hay paridad")

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
