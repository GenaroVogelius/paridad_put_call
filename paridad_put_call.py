import math


class ParidadPutCall():
    def __init__(self):
        self.e = math.e
    
    def calculate_call_price(self, put, S, K, r, T):
        precio_call = (put + S) - (K*self.e**(-r*T))
        return precio_call

    def calculate_put_price(self, call, S, K, r, T):
        precio_put = (call + K * self.e**(-r*T)) -S
        return precio_put

    def is_parity(self, call, put, S, K, r, T):
        return call + K * self.e**(-r * T) == put + S
    

    def calculate_limite_inferior_call(self, S, K, r, T):
        limite_inferior = max(S - K * self.e**(-r * T), 0)
        return round(limite_inferior, 2)

    def calculate_limite_inferior_put(self, S, K, r, T):
        
        limite_inferior = max(K * self.e**(-r * T) - S, 0)
        return round(limite_inferior, 2)


    def get_call_value_from_API(self):
        # TODO esto lo conectas a la API
        call = 24.090000000000003
        return call
    
    def get_put_value_from_API(self):
        # TODO esto lo conectas a la API
        put = 6.639993438941417
        return put




    def do_arbitraje_in_call(self, S, K, r, T):
        if self.get_call_value_from_API() < self.calculate_limite_inferior_call(S, K, r, T):
            return f"arbitro mediante la venta en corto de la acción(shorteo la acción) + compra del call, invierto los pesos a la tasa del {int(r*100)}% hasta el vencimiento de la opción."
        
    def do_arbitraje_in_put(self, S, K, r, T):
        if self.get_put_value_from_API() < self.calculate_limite_inferior_put(S, K, r, T):
            return f"arbitro comprando la acción a ${S} y comprando el put a ${self.get_put_value_from_API()}, financiando la inversión a {r*100}% anual por {int(T*365)} dias."



P = ParidadPutCall()
# print(P.do_arbitraje_in_call(S = 200, K = 190, r = 0.8, T = 0.2))

# print(P.do_arbitraje_in_put(S = 150, K = 190, r = 0.2, T = 0.2))
