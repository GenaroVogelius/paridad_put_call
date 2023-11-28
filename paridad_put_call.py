import math

# e ** rt es traido al valor presente, valor del precio de ejercicio traido al valor presente.

class ParidadPutCall():
    def __init__(self):
        self.e = math.e
    
    def call_sint_long(self, put, S, K, r, T):
        precio_call = (put + S) - (K*self.e**(-r*T))
        return precio_call

    def put_sint_long(self, call, S, K, r, T):
        precio_put = (call + K * self.e**(-r*T)) -S
        return precio_put
    

    def call_sint_short(self, put, S, K, r, T):
        precio_call = (-put - S) + (K*self.e**(-r*T))
        return precio_call
    
    def put_sint_short(self, call, S, K, r, T):
        precio_put = (-call - K * self.e**(-r*T)) + S
        return precio_put


    def is_parity(self, call, put, S, K, r, T):
        lado_call = round(call + K * self.e**(-r * T), 2)
        lado_put = round(put + S,2)

        if lado_call == lado_put:
            return "Hay paridad"
        elif lado_call < lado_put:
            return f"El call esta más barato en relación al put, ya que el call cuesta {lado_call} y el put {lado_put}, entonces deberias vender el put, comprar el call y con el dinero sobrante invertirlo a tasa"
        elif lado_call > lado_put:
            return f"El put esta mas barato en relación al call, ya que el call cuesta {lado_call} y el put {lado_put}, entonces deberias vender el call y comprar el put y la acción."

    

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
