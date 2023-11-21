from paridad_put_call import ParidadPutCall



Paridad = ParidadPutCall()


# si falta un año T = 0.1
# T tiene que ser siempre en años.
# Si tenes t, que seria meses, haces t/12 y listo
# si a t lo tenes en dias lo dividis por 365

# ejemplo:
# call = 0.7318
# put = 0.249676
# S = 19.13
# K = 20
# r = 0.7
# T = 0.1

# print(Paridad.is_parity(call, put, S, K, r, T))

# EJERCICIO ABAJO DEL CUADRITO DE APLICACIÓN DE PARIDAD PUT CALL
S=40; K=42; call=2; put=4; T=30/365; r= 0.30

# print(Paridad.is_parity(call, put, S, K, r, T))

# print(Paridad.call_sint_long(put, S, K, r, T))
# print(Paridad.call_sint_short(put, S, K, r, T))

print(Paridad.put_sint_short(call, S, K, r, T))

print(Paridad.put_sint_long(call, S, K, r, T))