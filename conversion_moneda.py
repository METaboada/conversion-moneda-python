
# Paso1: Definir el valor actual del eur y usd con respecto al mex
tipo_cambio_eur_a_mex = 23.70
tipo_cambio_usd_a_mex = 29.75

# en un caso realista esta información hay que traerla de una BDD o de una API

# Paso2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)
moneda = input("Ingrese la modena origen para la conversión EUR/USD: ")

# Paso3: Solicitar al usaurio el monto a convertir
monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso4: Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso5: Mostrar el resultado de la conversión al usuario
if moneda.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mex
    print("El resutlado de la conversion EUR a MEX es:", resultado)
elif moneda.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mex
    print("El resutlado de la conversion USD a MEX es:", resultado)
else:
    print ("No está disponible este tipo de conversión")
    
