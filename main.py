mayor = 0
residuo = 0
menor = 0
# Josué Bautista
numero1 = int(input('Ingrese un numero:'))
numero2 = int(input('Ingrese un numero:'))

if numero1 > numero2:
    mayor = numero1
    numero_menor = numero2

elif numero2 > numero1:
    mayor = numero2
    menor = numero1

elif numero1 == numero2:
    print('Ninguno es mayor')
# Sebastian Siquina
residuo = mayor % 2

if residuo == 0:
    print(f'El numero {mayor} es par porque su residuo es:', residuo)
else:
    print(f'El numero {mayor} impar porque su residuo es:', residuo)

# Eddy Poroj
